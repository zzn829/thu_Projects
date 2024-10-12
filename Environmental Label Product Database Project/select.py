# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pyodbc

conn=pyodbc.connect(           
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='LAPTOP-HMVL39A7\MSSQLSERVER_2022',
    Database='GreenMark',
    UID='sa',
    PWD='nicky127')
SQLcmd = 'select * from DateView'
Record = conn.execute(SQLcmd)
List = list(Record.fetchall())
print("標章號碼  產品名稱  型號 系列型號  生效日期  證書期限 ")
print("-------------------------------------------------")
for row in List:
    for col in row:
        print(col, end=' ')
    print()
#cursor = conn.cursor()
Record.close()
conn.close()
print("關閉資料庫")