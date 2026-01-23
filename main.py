import streamlit as st
import warnings
from backend.db_manager import DBManager
# --- 导入所有视图模块 (包括 Log 和 Performance) ---
from views import view_monitor, view_storage, view_index, view_health, view_logs, view_perf

# 屏蔽烦人的红色警告
warnings.filterwarnings("ignore", category=UserWarning)

# 设置页面配置
st.set_page_config(layout="wide", page_title="SQL Server Sentinel")

# 初始化 Session State
if 'connected' not in st.session_state:
    st.session_state['connected'] = False
if 'db_manager' not in st.session_state:
    st.session_state['db_manager'] = None

# --- 侧边栏逻辑 (Sidebar) ---
with st.sidebar:
    st.header("🔌 Connection")
    
    # 状态 A: 未连接 (显示登录框)
    if not st.session_state['connected']:
        server = st.text_input("Server", value="localhost")
        auth_mode = st.selectbox("Auth Mode", ["Windows", "SQL Server"])
        
        user = ""
        password = ""
        if auth_mode == "SQL Server":
            user = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
        database = st.text_input("Database", value="master")
        
        if st.button("Connect", type="primary"):
            mgr = DBManager(server, database, user, password, auth_mode)
            # 尝试连接
            if mgr.connect():
                st.session_state['db_manager'] = mgr
                st.session_state['connected'] = True
                st.rerun()
            else:
                st.error("Connection failed.")

    # 状态 B: 已连接 (显示菜单和断开按钮)
    else:
        mgr = st.session_state['db_manager']
        st.success(f"✅ Connected to {mgr.server}")
        
        st.markdown("---")
        
        # --- 导航菜单 (统一带图标，看起来更专业) ---
        nav = st.radio("Navigation", [
            "🔴 Live Monitor", 
            "💾 Storage Space", 
            "⚡ Index Health", 
            "🛡️ System Health",
            "📜 Log Analysis",
            "🚀 Performance History"
        ])
        
        st.markdown("---")
        if st.button("Disconnect", type="primary"):
            st.session_state['connected'] = False
            st.session_state['db_manager'] = None
            st.rerun()

# --- 主页面路由逻辑 ---
if st.session_state['connected'] and st.session_state['db_manager']:
    mgr = st.session_state['db_manager']
    
    # 根据菜单选择加载对应的视图
    if nav == "🔴 Live Monitor":
        view_monitor.render_view(mgr)
    elif nav == "💾 Storage Space":
        view_storage.render_view(mgr)
    elif nav == "⚡ Index Health":
        view_index.render_view(mgr)
    elif nav == "🛡️ System Health":
        view_health.render_view(mgr)
    elif nav == "📜 Log Analysis":
        view_logs.render_view(mgr)
    elif nav == "🚀 Performance History":
        view_perf.render_view(mgr)

else:
    # 欢迎页面 (Landing Page)
    st.title("👋 Welcome to SQL Server Sentinel")
    st.markdown("""
    ### All-in-One DBA Dashboard
    Please connect to a SQL Server instance using the sidebar.
    
    **Features:**
    * **🔴 Live Monitor**: Real-time deadlock & CPU tracking.
    * **💾 Storage**: Disk space & file growth analysis.
    * **⚡ Index Health**: Fragmentation detection & optimization advice.
    * **🛡️ System Health**: Backup verification & failed job alerts.
    * **📜 Log Analysis**: Security audit & system error scanning.
    * **🚀 Performance History**: Identify historical top CPU & I/O queries.
    """)