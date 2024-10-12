# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:19:45 2023

@author: User
"""

def check_num(n):
    SQLcmd = "select * from SSCview where 規格標準大分類編號='{}'".format(n)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()