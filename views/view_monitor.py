import streamlit as st
import time
# 修正后的导入语句
from backend.queries_monitor import fetch_blocking_chains, fetch_active_cpu, fetch_active_session_count

def render_view(mgr):
    st.title("🚀 Live Monitor")
    
    # Auto-Refresh Toggle
    if st.toggle("Auto-Refresh (3s)"):
        time.sleep(3)
        st.rerun()
        
    # Active Sessions Metric (这里调用了新加的后端函数)
    active_count_df = fetch_active_session_count(mgr)
    if not active_count_df.empty:
        st.metric("Active Sessions", active_count_df.iloc[0]['cnt'])
    else:
        st.metric("Active Sessions", 0)

    # Blocking Chains
    st.subheader("Blocking Chains")
    blocking_df = fetch_blocking_chains(mgr)
    
    if not blocking_df.empty:
        st.error("🚨 BLOCKING DETECTED!")
        st.dataframe(blocking_df)
        for index, row in blocking_df.iterrows():
            st.code(f"KILL {row['Blocker SPID']}; -- Kill the blocker", language="sql")
    else:
        st.success("No blocking chains detected.")

    # Active CPU
    st.subheader("Top CPU Consumers")
    cpu_df = fetch_active_cpu(mgr)
    st.dataframe(cpu_df)