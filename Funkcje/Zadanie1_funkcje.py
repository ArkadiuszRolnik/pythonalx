import unittest


#napisz funkcje, która sprawdzi czy dana liczba jest liczbą pierwszą

def czy_pierwsza(x):
    """Ten obszar nazywa się docstring i służy dokumentacji funkcji

    Sprawdza czy x jest liczbą pierwszą
    >>> czy_pierwsza(10)
    False
    >>> czy_pierwsza(7)
    True
    """
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

#print(help(czy_pierwsza))

#prymitywna forma testów
#assert czy_pierwsza(2) is True
#assert czy_pierwsza(11) is True
#assert czy_pierwsza(10) is False


#unittesty

class TestCzyPierwsza(unittest.TestCase):

    def test_czy_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(czy_pierwsza(7), True)
        self.assertEqual(czy_pierwsza(11), True)
        self.assertEqual(czy_pierwsza(19), True)
    def test_czy_pierwsza_dla_liczby_niepierwszej(self):
        self.assertEqual(czy_pierwsza(10), False)
        self.assertEqual(czy_pierwsza(36), False)