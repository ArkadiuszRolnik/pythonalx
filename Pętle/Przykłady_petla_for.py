napis = "Ala ma kota!"

for znak in napis:
    print(znak)

print("Wartość w znak po skończeniu pętli", znak)

elementy = (1, 'a', 2, 'c')

for e in elementy:
    print(e)

lista = [4, 12 ,11, 1]
for l in lista:
    print(l)

słownik = {1:"a", "Ala":"kot", "Albert":"Einstein"}

for k in słownik:
    print(k)

zbior = {1, 2, 3, "a"}

liczby =[1, 2, 3, 4, 5, 6, 7, 0, 10, 20, 30]
for liczba in liczby:
    if liczba ==0:
        break
    print(10/liczba)
else:
    print("Wykonałem się")
print("jestem po pętli")

liczby =[1, 2, 3, 4, 5, 6, 7, 0, 10, 20, 30]
for liczba in liczby:
    if liczba ==0:
        continue
    print(10/liczba)
else:
    print("Wykonałem się")
print("jestem po pętli")

print(range(10))
print(list(range(10)))