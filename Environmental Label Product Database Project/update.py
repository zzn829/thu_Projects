# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:55:56 2023

@author: User
"""

def update():
    try:
        sid=input('標章號碼: ')
        if check_sid(sid)!=None:
            print('沒有此標章號碼:{}'.format(sid))
            return 
        a = input('證書狀態: ')
        SQLcmd = "update GM set 證書狀態='{}' where 標章號碼='{}'".format(a,sid)
        conn.execute(SQLcmd)
        conn.commit()
        print('修改資料!')
    
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()

