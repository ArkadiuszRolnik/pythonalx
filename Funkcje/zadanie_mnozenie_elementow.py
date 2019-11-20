#napisz funckję

# a) iloczyn elementów z listy

def iloczyn(lista):
    wynik = 1
    for i in lista:
        wynik *= i
    return wynik

lista =[1,2,3,7]

print(iloczyn(lista))

#b)


#c) wybierze i zwróci z podanego napisu listę liczb
# x = "a1b2c1d"

def wybierz_cyfry(napis):
    wynik = []
    for litera in napis:
        if litera.isdigit():
            wynik.append(int(litera))
    return wynik

x = "a1b2c1d"

print(wybierz_cyfry(x))

#d) "a100b200" tak aby było 100, 200


