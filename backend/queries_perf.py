import pandas as pd

def fetch_top_cpu_queries(mgr):
    """Find top 20 queries by Total CPU Time."""
    sql = """
    SELECT TOP 20
        LEFT(t.text, 50) + '...' AS [Query Snippet],
        qs.execution_count AS [Exec Count],
        qs.total_worker_time / 1000 AS [Total CPU (ms)],
        qs.total_worker_time / qs.execution_count / 1000 AS [Avg CPU (ms)],
        qs.last_execution_time AS [Last Run],
        t.text AS [Full Query Text]
    FROM sys.dm_exec_query_stats qs
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) t
    ORDER BY qs.total_worker_time DESC
    """
    return mgr.run_query(sql)

def fetch_top_io_queries(mgr):
    """Find top 20 queries by Total Logical IO (Reads + Writes)."""
    sql = """
    SELECT TOP 20
        LEFT(t.text, 50) + '...' AS [Query Snippet],
        qs.execution_count AS [Exec Count],
        (qs.total_logical_reads + qs.total_logical_writes) AS [Total IO],
        (qs.total_logical_reads + qs.total_logical_writes) / qs.execution_count AS [Avg IO],
        qs.last_execution_time AS [Last Run],
        t.text AS [Full Query Text]
    FROM sys.dm_exec_query_stats qs
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) t
    ORDER BY (qs.total_logical_reads + qs.total_logical_writes) DESC
    """
    return mgr.run_query(sql)