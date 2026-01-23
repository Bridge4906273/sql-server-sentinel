import streamlit as st
from backend.queries_perf import fetch_top_cpu_queries, fetch_top_io_queries

def render_view(mgr):
    st.title("🚀 Performance History")
    st.markdown("Analyze historical query performance (cached plans) to identify resource bottlenecks.")

    tab_cpu, tab_io = st.tabs(["🔥 Top CPU Consumers", "💾 Top I/O Consumers"])

    # --- TAB 1: CPU ---
    with tab_cpu:
        st.subheader("Heavy Calculation Queries (High CPU)")
        if st.button("Scan CPU History"):
            df = fetch_top_cpu_queries(mgr)
            if not df.empty:
                st.dataframe(df.drop(columns=["Full Query Text"]), width="stretch")
                
                # Drill down interaction
                st.markdown("### Query Inspector")
                selected_idx = st.selectbox("Select a query to view full SQL:", df.index, format_func=lambda x: df.iloc[x]["Query Snippet"], key="cpu_select")
                st.code(df.iloc[selected_idx]["Full Query Text"], language="sql")
            else:
                st.info("No cached query plans found.")

    # --- TAB 2: IO ---
    with tab_io:
        st.subheader("Heavy Read/Write Queries (High I/O)")
        if st.button("Scan I/O History"):
            df = fetch_top_io_queries(mgr)
            if not df.empty:
                st.dataframe(df.drop(columns=["Full Query Text"]), width="stretch")
                
                # Drill down interaction
                st.markdown("### Query Inspector")
                selected_idx = st.selectbox("Select a query to view full SQL:", df.index, format_func=lambda x: df.iloc[x]["Query Snippet"], key="io_select")
                st.code(df.iloc[selected_idx]["Full Query Text"], language="sql")
            else:
                st.info("No cached query plans found.")