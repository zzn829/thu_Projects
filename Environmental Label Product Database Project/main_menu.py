

def main_menu():
    print('==環保標章產品資料表==')
    print('1.新增刪修資料表')
    print('2.查詢資料表')
    n=eval(input("請點選功能:"))
    if n==1:
        act()
    elif n==2:
        view()
