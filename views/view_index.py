import streamlit as st
from backend.queries_index import fetch_fragmentation

def render_view(mgr):
    st.title("🔍 Index Hygiene")
    
    st.info("Index analysis can be resource intensive.")
    
    if st.button("Analyze Indexes"):
        with st.spinner("Analyzing fragmentation..."):
            frag_df = fetch_fragmentation(mgr)
            
        if not frag_df.empty:
            st.dataframe(frag_df)
            
            for index, row in frag_df.iterrows():
                frag_percent = row['Fragmentation %']
                table = row['Table']
                idx = row['Index']
                
                if frag_percent > 50:
                    st.error(f"⚠️ {table}.{idx} ({frag_percent}%): Recommendation: REBUILD")
                elif frag_percent > 30:
                    st.warning(f"⚠️ {table}.{idx} ({frag_percent}%): Recommendation: REORGANIZE")
        else:
            st.success("No highly fragmented indexes found.")