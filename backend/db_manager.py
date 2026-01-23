import warnings
warnings.filterwarnings("ignore")
import pyodbc
import pandas as pd
import streamlit as st

class DBManager:
    def __init__(self, server, database, username, password, auth_type):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.auth_type = auth_type
        self.conn = None

    def get_connection_string(self):
        # Auto-detect driver
        drivers = [d for d in pyodbc.drivers() if 'ODBC Driver' in d]
        driver = 'SQL Server' # Fallback
        # Prioritize 18, 17, 13
        for v in ['18', '17', '13']:
            name = f'ODBC Driver {v} for SQL Server'
            if name in drivers:
                driver = name
                break
        
        if self.auth_type == "Windows":
            return f"DRIVER={{{driver}}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;TrustServerCertificate=yes;"
        else:
            return f"DRIVER={{{driver}}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};TrustServerCertificate=yes;"

    def connect(self):
        try:
            conn_str = self.get_connection_string()
            self.conn = pyodbc.connect(conn_str)
            return True
        except Exception as e:
            st.error(f"Connection Failed: {e}")
            return False

    def run_query(self, sql):
        if not self.conn:
            return pd.DataFrame()
        
        try:
            return pd.read_sql(sql, self.conn)
        except Exception as e:
            st.error(f"Query Failed: {e}")
            return pd.DataFrame()