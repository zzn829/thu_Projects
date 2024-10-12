# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:03:05 2023

@author: User
"""

def act():
    print('==環保標章產品資料表==')
    print('1.新增資料')
    print('2.修改資料')
    print('3.刪除資料')
    print('4.回主畫面')
    n=eval(input("請點選功能:"))
    if n==1:
        insert()
    elif n==2:
        update()
    elif n==3:
        delete()
    elif n==4:
        main_menu()
    else:
        print('請選擇1~4')