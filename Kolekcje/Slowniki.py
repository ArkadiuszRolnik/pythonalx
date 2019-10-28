# przypomnienie
# int, float, complex, str,
# list -> [], tuple -> ()
# dict -> {}

print(dict())
x = dict()
print(type(x))

pol_ang = {
    # "klucz": "wartosc"
    "klucz": "key",
    "wartosc": "value",
    "pies": "dog"
}

print(pol_ang)
print(pol_ang["pies"])
print("dog" in pol_ang)

if "dog" in pol_ang:
    print(pol_ang["dog"])

print(dir(pol_ang))

print(pol_ang.get("dog", "Brak takiego hasła"))
print(pol_ang.get("pies", "Brak takiego hasła"))

pol_ang['kot'] = "cat"

print(pol_ang)

print({1:"a", 2:"b"})
print({1.1:"a", 2.1:"b"})
print({(1, 2): "pierwsza"})
# kluczem mogą być liczby, napisy, tuple
# print({[1, 2]: "pierwsza"}) to się nie uda bo lista jest niehaszowalna

x = "1231231"
y = [1, 2, 3]

print(y,id(y))
y.append(4)
print(y,id(y))
print(pol_ang.keys())
print(pol_ang.values())
print(pol_ang.items())

print(dict(krowa="cow", dom = "house"))

print(pol_ang.pop("pies"))
print(pol_ang)

print(pol_ang.popitem()) #co to robi ?
print(pol_ang)

#set -> {}
# zbiór - kolekcja unikalnych i nieuporządkowanych wartości

zbior = {1, 2, 3, 4}
print(zbior, type(zbior))
print(dir(zbior))

zbior2 = {1, "a", 2, "b", "c", "z", 3}
print(zbior2)
zbior2.add(9)
print(zbior2)
zbior2.add("a")
print(zbior2)

lista = [1,1,1,1,1,1,1,1,1,2,2,2,4,5,5]
print(set(lista))

A = {1,2,3,4}
B = {3,4,5,6}
C = {1,2}
print("Suma zbiorow: ", A|B, A.union(B)) # dwa sposoby
print("Różnica zbiorow: ", A - B, A.difference(B))
print("Część wspólna, przecięcie: ", A & B, A.intersection(B))
print("Różnica symetryczna: ", A ^ B, A.symmetric_difference(B))
print("Podzbiór", A.issubset(C))
print("Podzbiór", C.issubset(A))

