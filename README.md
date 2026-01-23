\# SQL Server Sentinel 🛡️



!\[Python](https://img.shields.io/badge/Python-3.9%2B-blue)

!\[Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)

!\[SQL Server](https://img.shields.io/badge/SQL%20Server-DMV-lightgrey)

!\[License](https://img.shields.io/badge/License-MIT-green)



\## Project Overview



\*\*SQL Server Sentinel\*\* is a modular, high-performance database administration dashboard. It provides DBAs and Data Engineers with real-time visibility into SQL Server health, storage, and performance.



By leveraging Python and direct \*\*Dynamic Management View (DMV)\*\* queries, this tool provides an actionable "DBA Cockpit" that replaces traditional, slow monitoring methods like `sp\_who2` or SSMS Activity Monitor.



> \*\*Why I built this:\*\* In high-concurrency environments, blocking sessions can silently halt production pipelines. I created this tool to reduce the \*\*Mean Time to Resolution (MTTR)\*\* for database locks from minutes to seconds.



\## Key Features



\* \*\*🔴 Live Monitor\*\*: Real-time detection of blocking chains with dynamically generated `KILL` scripts to resolve deadlocks instantly.

\* \*\*💾 Storage Space\*\*: Integrated monitoring of OS-level drive capacity and DB-level `MDF`/`LDF` file growth using `sys.dm\_os\_volume\_stats`.

\* \*\*⚡ Index Health\*\*: Advanced fragmentation analysis (>30%) with smart maintenance advice: `REBUILD` vs. `REORGANIZE`.

\* \*\*🛡️ System Health\*\*: Automated audits for missing backups (24h) and failed SQL Agent job failures.

\* \*\*📜 Log Analysis\*\*: Security-focused auditing of Error Logs to identify brute-force login attacks and critical system errors via `xp\_readerrorlog`.

\* \*\*🚀 Performance History\*\*: Historical analysis of the \*\*Plan Cache\*\* to identify top CPU and I/O consuming queries.



\## Tech Stack \& Architecture



This project follows a strict \*\*MVC (Model-View-Controller)\*\* pattern to ensure high maintainability:



\* \*\*Frontend\*\*: \[Streamlit](https://streamlit.io/) for responsive navigation and real-time visualization.

\* \*\*Backend\*\*: Specialized query modules for direct database interaction.

\* \*\*Connector\*\*: `pyodbc` with a custom \*\*Driver Auto-Discovery\*\* algorithm.

\* \*\*Analytics\*\*: `pandas` for result set manipulation and `plotly` for capacity charting.



\## Quick Start



\### Prerequisites

\* Python 3.9+

\* SQL Server with `VIEW SERVER STATE` permissions.



\### Installation



1\.  \*\*Clone \& Navigate\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/Bridge4906273/sql-server-sentinel.git](https://github.com/Bridge4906273/sql-server-sentinel.git)

&nbsp;   cd sql-server-sentinel

&nbsp;   ```



2\.  \*\*Install Requirements\*\*

&nbsp;   ```bash

&nbsp;   pip install streamlit pandas pyodbc plotly

&nbsp;   ```



3\.  \*\*Launch App\*\*

&nbsp;   ```bash

&nbsp;   streamlit run main.py

&nbsp;   ```



\## File Structure



```text

sql-server-sentinel/

├── main.py                 # App routing \& Session State

├── db\_manager.py           # Connection \& Driver Detection

├── backend/                # Logic Layer: SQL Query Modules

│   ├── queries\_monitor.py  # Live session \& blocking logic

│   └── queries\_perf.py     # Plan cache \& performance logic

└── views/                  # UI Layer: Streamlit Views

&nbsp;   ├── view\_monitor.py     # Live Monitor UI

&nbsp;   └── view\_logs.py        # Log Analysis UI

