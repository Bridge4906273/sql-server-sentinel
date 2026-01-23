def fetch_missing_backups(mgr):
    sql = """
    SELECT 
        d.name AS [Database Name]
    FROM sys.databases d
    LEFT JOIN msdb.dbo.backupset b 
        ON d.name = b.database_name 
        AND b.type = 'D' 
        AND b.backup_finish_date > DATEADD(HOUR, -24, GETDATE())
    WHERE d.name NOT IN ('tempdb', 'model')
    GROUP BY d.name
    HAVING COUNT(b.backup_set_id) = 0
    """
    return mgr.run_query(sql)

def fetch_failed_jobs(mgr):
    sql = """
    SELECT 
        j.name AS [Job Name],
        h.run_date,
        h.run_time,
        h.message
    FROM msdb.dbo.sysjobhistory h
    JOIN msdb.dbo.sysjobs j ON h.job_id = j.job_id
    WHERE h.run_status = 0 
      AND CAST(CAST(h.run_date AS CHAR(8)) AS DATETIME) >= CAST(GETDATE()-1 AS DATE)
    ORDER BY h.run_date DESC, h.run_time DESC
    """
    return mgr.run_query(sql)