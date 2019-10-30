#losowanie

import random #ctrl + lmb aby odpalic podgląd modułu

print(dir(random))
print(help(random.randint))

print(random.randint(1,10))

gracz_x = random.randint(1,10)
gracz_y = random.randint(1,10)
skarb_x = random.randint(1,10)
skarb_y = random.randint(1,10)

print("Położenie gracza", gracz_x, gracz_y)
print("Położenie skarbu", skarb_x, skarb_y)

#abs wartość bezwzględna

odleglosc = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

print(odleglosc)

while True:
    instrukcja = input("By zakończyć wciśnij k:")
    if instrukcja == "k":
        break
