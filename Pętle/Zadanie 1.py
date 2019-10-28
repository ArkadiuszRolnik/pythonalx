#Zapytaj użytkownika o 10 liczb i wypisz ich średnią, skorzystaj z pętli for oraz z funkcji range

suma = 0
for x in range(3):
    x = int(input("Podaj liczbę"))
    suma = suma + x
print(suma/3)