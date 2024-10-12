# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:15:44 2023

@author: User
"""

def ssc():
    print('==標章規格標準分類表==')
    print('1.所有分類')
    print('2.依分類編號查詢')
    print('3.回主畫面')
    n=eval(input("請點選選項:"))
    if n==1:
        sscview()
    elif n==2:
        n_proc()
    elif n==3:
        main_menu()
    else:
        print('請選擇1~3')