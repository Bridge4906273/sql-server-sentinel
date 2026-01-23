def fetch_disk_usage(mgr):
    sql = """
    SELECT DISTINCT
        vs.volume_mount_point AS [Drive Letter],
        CAST(vs.total_bytes / 1073741824.0 AS DECIMAL(10,2)) AS [Total GB],
        CAST(vs.available_bytes / 1073741824.0 AS DECIMAL(10,2)) AS [Free GB],
        CAST((vs.available_bytes * 100.0) / vs.total_bytes AS DECIMAL(10,2)) AS [Free %]
    FROM sys.master_files mf
    CROSS APPLY sys.dm_os_volume_stats(mf.database_id, mf.file_id) vs
    """
    return mgr.run_query(sql)

def fetch_db_files(mgr):
    sql = """
    SELECT 
        name AS [File Name],
        size * 8 / 1024 AS [Size (MB)],
        CASE is_percent_growth 
            WHEN 1 THEN CAST(growth AS VARCHAR) + '%' 
            ELSE CAST(growth * 8 / 1024 AS VARCHAR) + ' MB' 
        END AS [Growth Setting]
    FROM sys.master_files
    """
    return mgr.run_query(sql)