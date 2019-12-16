#powtórka z obsługi plików
"""
fd = open("dane.txt", "rt")

for index, linia in enumerate(fd, 1): # zeby sie zaczynało od 1 a nie od 0
    print("krok", index,":",linia,end='') # nie dodowaj pustej linii

fd.close()
"""

with open("dane.txt", "rt") as fd:
    for index, linia in enumerate(fd, 1):
        print("krok", index, ":", linia, end='')

print("\nCzy plik zamknięty:",fd.closed)
