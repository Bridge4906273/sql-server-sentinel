import streamlit as st
import plotly.express as px
from backend.queries_storage import fetch_disk_usage, fetch_db_files

def render_view(mgr):
    st.title("💾 Storage Overview")
    
    # Disk Usage
    st.subheader("Disk Space")
    disk_df = fetch_disk_usage(mgr)
    if not disk_df.empty:
        fig = px.bar(disk_df, x='Drive Letter', y='Free GB', title="Free Space by Drive (GB)", text='Free GB')
        st.plotly_chart(fig)
        st.dataframe(disk_df)
    
    # DB Files
    st.subheader("Database Files")
    files_df = fetch_db_files(mgr)
    st.dataframe(files_df)