from random import randint

money = 0
moneyInfo = 1

print("""
      Rozpiska:
      Wpisz 1 aby kupic dom(jesli kupisz dom dostaniesz wiecej pieniedzy o 1 za przepisany kod! Dom kosztuje 50 zł)
      Wpisz 2 aby wyjsc
      Wpisz 3 aby zobaczyc ile masz pieniędzy
      Wpisz 4 aby zobaczyc ile aktualnie zarabiasz
      """)

while True:
    try:
        n = randint(0,9)
        n2 = randint(0,9)
        n3 = randint(0,9)
        n4 = randint(0,9)
        n5 = randint(0,9)
    	
        code = str(n)+str(n2)+str(n3)+str(n4)+str(n5)
        
        print("Kod:", code )
        information = input("Przepisz kod by dostać pięniądze lub wybierz co chcesz zrobic")

        if information == code:
            money += moneyInfo
            print("Dodano do twojego konta", moneyInfo, "zł!", "Aktualnie masz", money, "zł na koncie")
        elif information == "3":
            print("Twoje pieniądze:", money)
        elif information == "2":
            break
        elif information == "1":
            if int(money) == 50:
                moneyInfo += 1
                print("Gratulajce! Zarabiasz teraz:", moneyInfo, "zł za kod")
            else:
                print("Nie masz 50 zł")
        elif information == "4":
            print("Aktualnie za kod zarabiasz:", moneyInfo, "zł")
    except: print("Wystąpił błąd")