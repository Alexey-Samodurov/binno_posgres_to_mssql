import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from local_config import PG_USER, PG_PASSWORD, PG_HOST

MSSQL_CONN = (
    r'DRIVER={SQL Server};'
    r'SERVER=158.160.53.140;'
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


def get_data_from_mssql():
    return pd.read_sql(sql='select * from binnopharm_personal_data_uploaded',
                       con=create_engine('mssql+pyodbc:///?odbc_connect={}'.format(MSSQL_CONN)),
                       chunksize=1000,
                       )


def upload_data_to_postgres():
    for chunk in get_data_from_mssql():
        print('insert into posgrtes {} rows'.format(len(chunk)))
        chunk.astype(str).to_sql('__binnopharm_personal_data_uploaded',
                                 create_engine(POSTGRES_CONN),
                                 if_exists='append',
                                 index=False)


if __name__ == '__main__':
    upload_data_to_postgres()
