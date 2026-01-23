import streamlit as st
from backend.queries_health import fetch_missing_backups, fetch_failed_jobs

def render_view(mgr):
    st.title("🏥 System Health")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Missing Backups (24h)")
        backups_df = fetch_missing_backups(mgr)
        if not backups_df.empty:
            st.warning("The following databases have not been backed up in the last 24 hours:")
            st.dataframe(backups_df)
        else:
            st.success("All databases backed up recently.")
            
    with col2:
        st.subheader("Failed Jobs (24h)")
        jobs_df = fetch_failed_jobs(mgr)
        if not jobs_df.empty:
            st.error("The following jobs failed recently:")
            st.dataframe(jobs_df)
        else:
            st.success("No failed jobs found.")