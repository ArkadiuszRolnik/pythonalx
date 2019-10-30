#definicja funkcji
def nazwa_funkcji(): #ta funkcja nie przyjmuje argumentów
    # to ciało funkcji
    # blok instrukcji
    print("Hello World!!")

#wywołanie
nazwa_funkcji()

def funkcja_z_argumentem(x):
    """
    x - argument mojej funkcji. Mogę go używać wewnątrz niej
    będzie dostępny pod nazwą x
    :param x:
    :return:
    """
def do_piatej(liczba):
    #print(liczba**5)
    return liczba**5

x = do_piatej(4)
print(x)

def duze_litery(napis):
    return napis.upper()

print(duze_litery("sdfsdf"))
