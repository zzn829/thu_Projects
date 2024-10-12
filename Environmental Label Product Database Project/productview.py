# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:57:40 2023

@author: User
"""

def product():
    try:
        SQLcmd = 'select * from ProductView'
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print("標章號碼  產品名稱  型號 系列型號   公司名稱    工廠名稱    工廠地址")
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