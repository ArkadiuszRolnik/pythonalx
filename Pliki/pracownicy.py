# "baza danych" pracowników

import datetime


dane_pracownikow = list () # miejsce przechowujące dane na temat rekordów pracowników

def wprowadz_dane():
    print("="*40)
    print("Wprowadz dane pracownika")

    imie = None
    while(True):
        imie = input("Podaj imie: ").upper().strip()
        if len(imie) <=2:
            print("Podaj imię")

    nazwisko = None
    while True:
        nazwisko = input("Podaj nazwisko: ").upper().strip()
        if len(nazwisko) >= 3:
            break
    print("Podaj nazwisko")


    rok_urodzenia = None

    while True:
        try:
            rok_urodzenia = int(input("Podaj rok urodzenia: "))
            if rok_urodzenia < 1930:
                print("Idź na emeryturę")
                continue

            rok_biezacy = datetime.datetime.now().year
            if rok_biezacy - rok_urodzenia >=15:
            break
            print("Za młodyś na pracę")


        except Exception as exc:
            print("Podaj rok urodzenia",exc)


    pensja = None

    while True:
        try:
            pensja = float(input("Podaj wartość wynagrodzenia: "))
            if pensja > 0:
               break
            print("Podaj wartość wynagrodzenia: ")
            continue


        except Exception as exc:
            print("Podaj wartość wynagrodzenia:", exc)


    pass


while(True):
    operacja = input("Podaj operację [d/w/q]: ").strip().upper()
    if operacja=="Q":
        print("Koniec aplikacji")
        break

    if operacja=="W":
        pass

    if operacja=="D":
        wprowadz_dane()