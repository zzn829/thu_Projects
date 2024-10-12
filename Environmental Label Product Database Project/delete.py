# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:51:46 2023

@author: User
"""

def delete():
    try:
        sid=input('標章號碼: ')
        if check_sid(sid)!=None:
            print('沒有此標章號碼:{}'.format(sid))
            return 
        SQLcmd = "delete from GM where 標章號碼='{}'".format(sid)
        conn.execute(SQLcmd)
        conn.commit()
        print('刪除資料!!')
    
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()

