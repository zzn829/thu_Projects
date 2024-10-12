# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:01:00 2023

@author: User
"""

def date():
    print('==標章產品有效期限表==')
    print('1.所有年份')
    print('2.依年份查詢')
    print('3.回主畫面')
    n=eval(input("請點選選項:"))
    if n==1:
        dateview()
    elif n==2:
        cp_proc()
    elif n==3:
        main_menu()
    else:
        print('請選擇1~3')