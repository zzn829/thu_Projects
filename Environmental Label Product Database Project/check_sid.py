# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:15:58 2023

@author: User
"""

def check_sid(sid):
    SQLcmd = "select * from GM where 標章號碼='{}'".format(sid)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()