def fetch_fragmentation(mgr):
    sql = """
    SELECT 
        OBJECT_NAME(ips.object_id, DB_ID()) AS [Table],
        i.name AS [Index],
        CAST(ips.avg_fragmentation_in_percent AS DECIMAL(5,2)) AS [Fragmentation %]
    FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips
    JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
    WHERE ips.avg_fragmentation_in_percent > 30 
      AND ips.page_count > 50
    ORDER BY ips.avg_fragmentation_in_percent DESC
    """
    return mgr.run_query(sql)