# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:42:28 2023

@author: User
"""

def cp_proc():

    try:
        y=input('證書期限: ')
        if check_year(y)!=None:
            print('沒有此證書期限:{}'.format(y))
            return        
        SQLcmd = "exec cp_year_proc @cp='{}'".format(y)
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print('標章號碼  產品名稱  型號     系列型號    生效日期    證書期限 ')
        print('----------------------------------------------------------')
        
        for row in List:
            for col in row:
                print(col, end='|')
            print()
        conn.commit()
        print('查詢成功')
        
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()