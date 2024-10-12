# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 18:08:38 2023

@author: User
"""

def check_year(y):
    SQLcmd = "select * from DateView where 證書期限='{}'".format(y)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()