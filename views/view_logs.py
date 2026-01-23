import streamlit as st
from backend.queries_logs import fetch_error_logs

def render_view(mgr):
    st.title("📜 Log & Error Analysis")
    st.markdown("Analyzes the **SQL Server Error Log** to detect security threats and critical failures.")

    # Manual Trigger to avoid reading huge logs automatically
    if st.button("📥 Scan Error Logs"):
        with st.spinner("Reading SQL Server logs... (This might take a moment)"):
            df_logs = fetch_error_logs(mgr)

        if not df_logs.empty:
            # Create Tabs for different analysis focus
            tab_security, tab_system, tab_raw = st.tabs(["🔴 Security Audit", "⚠️ System Errors", "📄 Raw Log"])

            # --- Tab 1: Security (Brute Force Detection) ---
            with tab_security:
                st.subheader("Failed Login Attempts")
                # Filter for login failures
                df_security = df_logs[df_logs['Text'].str.contains("Login failed", case=False, na=False)]
                
                if not df_security.empty:
                    st.error(f"🚨 Found {len(df_security)} failed login attempts!")
                    st.dataframe(df_security, width="stretch")
                else:
                    st.success("No failed login attempts found in current log.")

            # --- Tab 2: System Errors (Severity/Critical) ---
            with tab_system:
                st.subheader("Critical System Errors")
                # Filter for specific error keywords
                error_keywords = ["Error: ", "Severity:", "Corrupt", "IO Request", "Yield"]
                # Regex logic to join keywords with OR (|)
                pattern = '|'.join(error_keywords)
                
                df_errors = df_logs[df_logs['Text'].str.contains(pattern, case=False, na=False)]
                
                if not df_errors.empty:
                    st.warning(f"⚠️ Found {len(df_errors)} potential system errors.")
                    st.dataframe(df_errors, width="stretch")
                else:
                    st.success("No critical system errors detected.")

            # --- Tab 3: Raw Data ---
            with tab_raw:
                st.subheader("Full Log Viewer")
                st.dataframe(df_logs, width="stretch")

        else:
            st.warning("Log is empty or permission denied (Requires VIEW SERVER STATE).")