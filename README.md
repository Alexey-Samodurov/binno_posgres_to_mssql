# binno_posgres_to_mssql
## How to run
1. Set your ```local_config.py``` file in root dir
2. Add Variables in ```local_config.py```:
   - PG_USER - postgres user
   - PG_PASSWORD - postgres password
   - PG_HOST - postgres host
3. Run following commands:
   - ```docker build -t mssql .```
   - ```docker run -p 1433:1433 mssql```
   - ```python mssql_to_posgres.py```
   - ```python posgres_to_mssql.py```
