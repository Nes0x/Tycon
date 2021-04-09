import random

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
        randomCode = ["wadjiuwahidaw", "duiawhduyasdaw", "wdjisahudnawolfkiaushndfk", "widhausyhdacmbwd9uwahdusaf",
                  "wajdishagcnvjwa8aopd", "dw9wadsaodjwioad2890323", "223-192931102", "283082139-12391-54123781", "2301823816815125", "23928187391231"]

        randomCodeLen = len(randomCode) - 1
        randomCodeRand = random.randint(0, randomCodeLen)

        a = (randomCode[randomCodeRand])
        print("Kod:", a)
        information = input("Przepisz kod by dostać pięniądze lub wybierz co chcesz zrobic")

        if information == a:
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