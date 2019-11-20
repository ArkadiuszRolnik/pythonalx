def przytnij(lista,start,stop):
    wynik = []
    czy_dodawac = False
    for el in lista:
        if czy_dodawac or start(el):
            czy_dodawac = True
            wynik.append(el)
            if stop(el):
                break
    return wynik

def test_przytnij():

    result = przytnij(lista=[1,2,3,4,1,6,7], start=lambda x: x==2, stop=lambda x: x+1 >6)
    assert result == [2,3,4,1,6]

    result = przytnij(lista=[8,9,3,1,5,12,19,21,0], start=lambda x: x % 3 == 0, stop=lambda x: x % 4 == 0)
    assert result == [9,3,1,5,12]
