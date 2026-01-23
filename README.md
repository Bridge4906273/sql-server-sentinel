SQL Server Sentinel 🛡️
Project Overview
SQL Server Sentinel is a modular, high-performance database administration dashboard. It provides DBAs and Data Engineers with real-time visibility into SQL Server health, storage, and performance.

By leveraging Python and direct Dynamic Management View (DMV) queries, this tool provides an actionable "DBA Cockpit" that replaces traditional, slow monitoring methods.

Development Philosophy: Built to minimize the "Mean Time to Resolution" (MTTR) for critical database incidents—from deadlocks to disk space exhaustion.

Key Features
🔴 Live Monitor: Real-time detection of blocking chains with dynamically generated KILL scripts.

💾 Storage Space: Integrated monitoring of OS-level drive capacity and DB-level MDF/LDF file growth.

⚡ Index Health: Advanced fragmentation analysis (>30%) with maintenance advice (Rebuild vs. Reorganize).

🛡️ System Health: Automated audits for backup gaps in the last 24 hours and SQL Agent job failures.

📜 Log Analysis: Security-focused auditing of Error Logs to identify brute-force login attacks and critical system errors.

🚀 Performance History: Historical analysis of the Plan Cache to identify top CPU and I/O consuming queries over time.

Tech Stack \& Architecture
This project follows a strict MVC (Model-View-Controller) pattern to ensure high maintainability and scalability:

Frontend (View): Built with Streamlit for responsive navigation and real-time data visualization.

Backend (Model): Specialized query modules designed for direct database interaction and data processing.

Connector: Uses pyodbc with a custom Driver Auto-Discovery algorithm to ensure seamless connectivity across different environments.

Analytics: Leverages pandas for result set manipulation and plotly for dynamic capacity charting.

Quick Start
Prerequisites
Python 3.9+

SQL Server (Local or Remote)

Account permissions: VIEW SERVER STATE and access to msdb.

Installation
Clone the repository

Bash

git clone https://github.com/Bridge4906273/sql-server-sentinel.git
cd sql-server-sentinel
Install dependencies

Bash

pip install streamlit pandas pyodbc plotly
Run the application

Bash

streamlit run main.py
Connect: Use the Sidebar Portal to enter your credentials (Windows or SQL Auth). Once connected, all monitoring modules will be unlocked.

Demo Screenshots
Healthy State Dashboard: Monitoring active sessions with 0 blocked processes.

Storage Analysis: Visualizing drive capacity and database file growth tables.

Maintenance Audit: Identifying missing backups and failed Agent jobs.

File Structure
Plaintext

sql-server-sentinel/
├── main.py                 # Core Entry: App routing \& Session State
├── db\_manager.py           # Backend Core: Connection \& Driver Detection
├── requirements.txt        # Project dependencies
├── backend/                # Logic Layer: Specialized SQL query modules
│   ├── queries\_monitor.py  # Live session \& blocking logic
│   ├── queries\_logs.py     # Log auditing logic
│   └── queries\_perf.py     # Plan cache \& performance logic
└── views/                  # UI Layer: Streamlit-based functional views
├── view\_monitor.py     # Live Monitor UI
├── view\_perf.py        # Performance History UI
└── view\_logs.py        # Log Analysis UI

