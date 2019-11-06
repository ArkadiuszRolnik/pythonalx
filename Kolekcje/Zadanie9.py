'''

Oferujemy następujące produkty

marchew: 2.35, ziemniaki: 2.2, cebula: 1.8, ogórki: 4.0

co chcesz kupić ? marchew
ile chcesz kupić [marchew]

Za [marchew] zapłacisz

2. Dodajemy obsługę magazynu
po zakupie ilość towaru się zmniejsza, jeśli ktoś chce kupić więcej niż jest w magazynie to mówię niż nie może

'''

towary = {"marchew":2.35,
            "ziemniaki":2.2,
            "cebula":1.8,
            "ogórki":4.0}

magazyn = {"marchew":40,
           "ziemniaki":40,
           "cebula":40,
           "ogórki":40}

print("""

Witaj w naszym PyZieleniaku!

Oferujemy następujące produkty:
     
""")

for towar in towary:
    print(f" - {towar}:{towary[towar]}")

while True:
    tryb = input("Wybierz tryb: [z-zakupowy, m-magazynowy, k-kończymy]")
    if tryb == 'k':
        break
    elif tryb == 'z':
        while True:
            co_kupuje = input("Jaki towar chcesz kupić ? (wpisz k by zakończyć) ")
            if co_kupuje == 'k':
                break
            if co_kupuje in towary:
                ile = input(f"Ile chcesz kupić [{co_kupuje}]")
                ile = float(ile)
                if ile < magazyn[co_kupuje]:
                    naleznosc = ile * towary[co_kupuje]
                    magazyn[co_kupuje] = magazyn[co_kupuje] - ile
                    print(f"Za [{co_kupuje}] placisz {naleznosc:.2f} PLN")
                else:
                    print("Za mało towaru")
            else:
                print("Nie ma takiego towaru !")
    elif tryb == 'm':
        while True:
            print("W magazynie: ")
            for towar, ilosc in magazyn.items()
            produkt_do_dodania = input("Co chcesz dodać ?")
            ile_do_dodania = int(input("Ile chcesz dodać ?"))

            if not produkt_do_dodania in towary:
                cena_nowego_pr = float(input("Jaka będzie cena ?"))
                towary[produkt_do_dodania] = cena_nowego_pr
            magazyn[produkt_do_dodania] = magazyn.get(produkt_do_dodania, 0) + ile_do_dodania