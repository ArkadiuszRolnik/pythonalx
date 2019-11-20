"""funkcje anonimowe"""

x = lambda a,b : a*b

print(x(10,6))

def fun_sort(x):
    return x[1]


lista=[("Winogrona", 7.99), ("Jabłko", 2.99), ("Banan", 4.99)]
print(sorted(lista, key=lambda x:x[1]))

#Napisz funkcję, która z zadanej listy liczb wybierze elementy określone przez funkcję klucza

#lista = [1, 2, 3, 4, 5, 6]
#wybierz(lista, key = lambda x: x%2 == 0)
#[2, 4, 6]

lista = [1, 2, 3, 4, 5, 6]
def wybierz(lista, funkcja):
    wynik = []
    for el in lista:
        if funkcja(el) is True:
            wynik.append(el)
    return wynik

print(wybierz(lista, lambda x: x%3 == 0))

def wieksz_niz4(x):
    return x > 4

print(wybierz(lista, wieksz_niz4))


data = [1, 2, 3, 4, 5, 6, 7, 8]

def przytnij(data, start, stop):
    wynik = []
    for el in data:
        if start(el) is True and stop(el) is False:
            wynik.append(el)
        elif start(el) is True and stop(el) is True:
            wynik.append(el)

        return wynik
print(przytnij(data, lambda x: x > 0, lambda x:x == 6))
