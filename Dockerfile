FROM mcr.microsoft.com/mssql/server:2019-latest

ENV MSSQL_SA_PASSWORD=Some_H@rd_Password \
    ACCEPT_EULA=Y \
    COLLATION=UTF-8