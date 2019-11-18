"""
Funkcja z dowolną liczbą parametrów
"""

#funkcja mnożny wartości podane do jej środka
#możliwe podanie nieznanj liczyby argumentów

def iloczyn(*args): #to może być dowolna nazwa zamiast args
    wynik = 1
    for _, arg in enumerate (args,1): # to bedzie krotka, tupla inna wersja to _, arg wtedy nie musimy pisać wynik *= arg[1] tylko wynik *= arg
        #print(f"Pozycja {nr} = {arg}")
        wynik *= arg
    return wynik

print(iloczyn(1,2,3,6,7,10))

