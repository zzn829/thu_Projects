# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def dateview():
    try:
        SQLcmd = 'select * from DateView'
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print("標章號碼  產品名稱  型號 系列型號  生效日期  證書期限 ")
        print("-------------------------------------------------")
        for row in List:
            for col in row:
                print(col, end=' ')
            print()
        #cursor = conn.cursor()
        Record.close()
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()
