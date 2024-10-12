# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:03:30 2023

@author: User
"""

def view():
    print('==環保標章產品資料表==')
    print('1.標章產品有效期限表')
    print('2.標章規格標準分類表')
    print('3.標章產品細節表')
    print('4.回主畫面')
    n=eval(input("請點選想查看的資料:"))
    if n==1:
        date()
    elif n==2:
        ssc()
    elif n==3:
        product()
    elif n==4:
        main_menu()
    else:
        print('請選擇1~4')