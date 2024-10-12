# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:21:54 2023

@author: User
"""

def insert():
    try:
        sid=input('標章號碼: ')
        if check_sid(sid)!=None:
            print('標章號碼:{}重複了'.format(sid))
            return 
        a = input('證書狀態: ')
        b = input('類別: ')
        d = input('產品名稱: ')
        e = input('型號: ')
        f = input('系列型號: ')
        g = input('公司名稱: ')
        h = input('工廠名稱: ')
        i = input('工廠地址: ')
        j = input('規格標準大分類: ')
        k = input('規格標準大分類編號: ')
        l = input('規格標準_環境訴求: ')
        m = input('規格標章編號: ')
        n = input('生效日期: ')
        o = input('證書期限: ')
        p = input('驗證機構: ')
        SQLcmd = """insert into GM values('{}','{}','{}','{}','{}',
        '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
        '{}')""".format(a,b,sid,d,e,f,g,h,i,j,k,l,m,n,o,p)
        conn.execute(SQLcmd)
        conn.commit()
        print('新增資料~')
    
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()

