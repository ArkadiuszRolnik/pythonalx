"""
utwórz klasę produkt, która będzie działać"
 pr = Product(1, "woda", 10.99)

#>>>pr.id
#>>>1

#>>>pr.show()
#>>> "Woda (1)m cena: 10.99"
"""

class Product:

    NEXT_ID = 1 # atrybut klasowy

    def __init__(self, name, price):

        self.id = self.NEXT_ID # pobierz atrybut klasowy i przypisz go do instancji
        self.name = name
        self.price = price
        self.incr_next_id()

    @classmethod

    def incr_next_id(cls):
        cls._NEXT_ID +=1


    def show(self):
        print(f"{self.name} ({self.id}), cena: {self.price}")




def test_product():
    pr = Product("woda", 10.99)
    pr2 = Product("wóda", 10.99)
    assert pr.id == 1
    assert pr.name == "woda"
    assert pr.price == 10.99
    assert pr.id == 2
    assert pr.name == "wóda"
    assert pr.price == 10.99

def test_product_show():
    pr = Product(1, "woda", 10.99)
    assert pr.show() == "woda (1), cena: 10.99"