"""
Zaimplementuj klase Vector dostarczajaca funkcjonalnosc wektora
swobodnego na dwuwymiarowej płaszczyznie. Wektory powinny
miec mozliwosc dodawania, odejmowania, mnozenia (przez inny
wektor i przez liczbe), porównywania (po długosci) oraz powinny
posiadac czytelna reprezentacje napisowa.
Przykład uzycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
