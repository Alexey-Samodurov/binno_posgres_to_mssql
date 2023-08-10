import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from local_config import PG_USER, PG_PASSWORD, PG_HOST

MSSQL_CONN = (
    r'DRIVER={SQL Server};'
    r'SERVER=localhost;'
    r'UID=sa;'
    r'PWD=Some_H@rd_Password;'
)

POSTGRES_CONN = URL.create(
    drivername='postgresql+psycopg2',
    username=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=6432,
    database='binnopharm'
)


def get_data_from_postgres():
    return pd.read_sql('select * from binnopharm_personal_data_uploaded',
                       create_engine(POSTGRES_CONN),
                       chunksize=1000
                       )


def upload_data_to_mssql():
    for chunk in get_data_from_postgres():
        print('insert into mssql {} rows'.format(len(chunk)))
        chunk.astype(str).to_sql('binnopharm_personal_data_uploaded',
                                 create_engine('mssql+pyodbc:///?odbc_connect={}'.format(MSSQL_CONN)),
                                 if_exists='append',
                                 index=False)


if __name__ == '__main__':
    upload_data_to_mssql()
