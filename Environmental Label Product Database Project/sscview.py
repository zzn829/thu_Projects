# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:55:24 2023

@author: User
"""

def sscview():
    try:
        SQLcmd = 'select * from SSCview'
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print("標章號碼  產品名稱  型號 系列型號  規格標準大分類 規格標準大分類編號 ")
        print("---------------------------------------------------------------")
        for row in List:
            for col in row:
                print(col, end=' ')
            print()
        #cursor = conn.cursor()
        Record.close()
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()