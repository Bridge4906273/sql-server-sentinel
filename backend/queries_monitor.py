def fetch_blocking_chains(mgr):
    sql = """
    SELECT 
        r.session_id AS [Victim SPID],
        r.blocking_session_id AS [Blocker SPID],
        r.wait_time AS [Wait Time],
        t.text AS [Query Text]
    FROM sys.dm_exec_requests r
    CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
    WHERE r.blocking_session_id <> 0
    """
    return mgr.run_query(sql)

def fetch_active_cpu(mgr):
    sql = """
    SELECT TOP 20
        r.session_id AS [SPID],
        r.cpu_time AS [CPU Time],
        r.status AS [Status],
        LEFT(t.text, 100) AS [Query Snippet]
    FROM sys.dm_exec_requests r
    CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
    ORDER BY r.cpu_time DESC
    """
    return mgr.run_query(sql)

def fetch_active_session_count(mgr):
    sql = "SELECT COUNT(*) as cnt FROM sys.dm_exec_sessions WHERE status = 'running'"
    return mgr.run_query(sql)