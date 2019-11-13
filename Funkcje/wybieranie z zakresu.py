'''
lista = [-2, 10, 0, 5, 1, 16, 9]
wybierz_z_przedzialu(lista, 5, 10)
[10, 5, 9]
'''

lista = [-2, 10, 0, 5, 1, 16, 9]

def wybierz_z_przedzialu(lista, a, b):
    wynik = []
    for i in lista:
        if a <= i <= b:
            wynik.append(i)
    return wynik


def test_wybierz_z_przedzialu_pusta_lista():
    assert wybierz_z_przedzialu([], 10, 20) == []

def test_wybierz_z_przedzialu():
    assert wybierz_z_przedzialu(lista, 5, 10) == [10, 5, 9]
