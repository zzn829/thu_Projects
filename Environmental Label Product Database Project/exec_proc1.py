# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:17:53 2023

@author: User
"""

def n_proc():

    try:
        n=input('規格標準大分類編號: ')
        if check_num(n)!=None:
            print('沒有此規格標準大分類編號:{}'.format(n))
            return        
        SQLcmd = "exec ssc_n_proc @n='{}'".format(n)
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print('標章號碼  產品名稱  型號     系列型號   規格標準大分類 規格標準大分類編號')
        print('-------------------------------------------------------------------')
        
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