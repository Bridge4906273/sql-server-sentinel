import pandas as pd

def fetch_error_logs(mgr):
    """
    Executes xp_readerrorlog to get the current SQL Server Error Log.
    Returns a DataFrame with columns: [LogDate, ProcessInfo, Text]
    """
    # 0 = Current Log file, 1 = SQL Server Log (not Agent log)
    sql = "EXEC sys.xp_readerrorlog 0, 1"
    df = mgr.run_query(sql)
    
    # Check if dataframe is empty (e.g. permission issues)
    if df.empty:
        return df

    # Ensure LogDate is datetime for sorting
    if 'LogDate' in df.columns:
        df['LogDate'] = pd.to_datetime(df['LogDate'])
        df = df.sort_values(by='LogDate', ascending=False)
        
    return df