from random import randint
from enum import IntEnum

money = 0
moneyInfo = 1
information = ''
Menu = IntEnum("Menu", "BuyHouse Money CodeInfo Exit")



print("""Rozpiska:
Wpisz 1 aby kupić dom(jeśli kupisz dom dostaniesz 1 zł więcej za przepisany kod! Dom kosztuje 50 zł)
Wpisz 2 aby zobaczyć ile masz pieniędzy
Wpisz 3 aby zobaczyć ile aktualnie zarabiasz
Wpisz 4 aby wyjść""")

while information != Menu.Exit:
    try:
        n = randint(0,9)
        n2 = randint(0,9)
        n3 = randint(0,9)
        n4 = randint(0,9)
        n5 = randint(0,9)
    	
        code = str(n)+str(n2)+str(n3)+str(n4)+str(n5)
        
        print("Kod:", code )
        information = int(input("Przepisz kod by dostać pięniądze lub wybierz co chcesz zrobić"))

        if str(information) == code:
            money += moneyInfo
            print("Dodano do twojego konta", moneyInfo, "zł!", "Aktualnie masz", money, "zł na koncie")
        elif information == Menu.BuyHouse:
           if int(money) >= 50:
                moneyInfo += 1
                money -= 1
                print("Gratulajce! Zarabiasz teraz:", moneyInfo, "zł za kod")
           else:
                print("Nie masz 50 zł")
        elif information == Menu.Money:
            print("Twoje pieniądze:", money)
        elif information == Menu.CodeInfo:
            print("Aktualnie za kod zarabiasz:", moneyInfo, "zł")
    except: print("Wystąpił błąd")
