def product():
    try:
        SQLcmd = 'select * from ProductView'
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print("標章號碼  產品名稱  型號 系列型號   公司名稱    工廠名稱    工廠地址")
        print("---------------------------------------------------------------")
        
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
    
def check_num(n):
    SQLcmd = "select * from SSCview where 規格標準大分類編號='{}'".format(n)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()

def n_proc():
    try:
        n=input('規格標準大分類編號: ')
        if check_num(n) == None:
            print('沒有規格標準大分類編號:{}'.format(n))
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



def sscview():
    try:
        SQLcmd = 'select * from SSCview'
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print("標章號碼  產品名稱  型號 系列型號  規格標準大分類 規格標準大分類編號 ")
        print("---------------------------------------------------------------")
        
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
        
def check_year(y):
    SQLcmd = "select * from DateView where 證書期限='{}'".format(y)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()

def cp_proc():
    try:
        y=input('證書期限: ')
        if check_year(y) != None:
            print('沒有此證書期限:{}'.format(y))
            return        
        SQLcmd = "exec cp_year_proc @cp='{}'".format(y)
        Record = conn.execute(SQLcmd)
        List = list(Record.fetchall())
        print('標章號碼  產品名稱  型號     系列型號    生效日期    證書期限 ')
        print('----------------------------------------------------------')
        
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
        
def check_sid(sid):
    SQLcmd = "select * from GM where 標章號碼='{}'".format(sid)
    cursor = conn.execute(SQLcmd)
    return cursor.fetchone()

def delete():
    try:
        sid=input('標章號碼: ')
        if check_sid(sid) == None:
            print('沒有標章號碼:{}'.format(sid))
            return 
        SQLcmd = "delete from GM where 標章號碼='{}'".format(sid)
        conn.execute(SQLcmd)
        conn.commit()
        print('刪除資料!!')
    
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()

def update():
    try:
        sid=input('標章號碼: ')
        if check_sid(sid) == None:
            print('沒有標章號碼:{}'.format(sid))
            return 
        a = input('證書狀態: ')
        SQLcmd = "update GM set 證書狀態='{}' where 標章號碼='{}'".format(a,sid)
        conn.execute(SQLcmd)
        conn.commit()
        print('修改資料!')
    
    except Exception as e:
        conn.rollback()
        print(f"操作失败：{e}")
    main_menu()

def insert():
    try:
        sid=input('標章號碼: ')
        if check_sid(sid)!= None:
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

def main_menu():
    print('==環保標章產品資料表==')
    print('1.新增刪修資料表')
    print('2.查詢資料表')
    n=eval(input("請點選功能:"))
    if n==1:
        act()
    elif n==2:
        view()

import pyodbc

conn=pyodbc.connect(           
    Driver='{ODBC Driver 17 for SQL Server}',
    Server='LAPTOP-HMVL39A7\MSSQLSERVER_2022',
    Database='GreenMark',
    UID='sa',
    PWD='nicky127')
try:
    while True:
        main_menu()
        
except KeyboardInterrupt:
    print('out')
    
finally:
    conn.close()
    print("關閉資料庫")