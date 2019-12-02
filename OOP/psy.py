# definicja klasy
class Pies:

    gatunek = "Canis Familiaris"
    ile = 0

    def __init__(self, imie, waga):
        self.imie = imie
        self.waga = waga
        Pies.ile += 1

    def szczekaj(self):
        print(f"{self.imie} szczeka")
    pass


# tworzę instancję klasy Pies
# jest przypisana do zmiennej Azor


azor = Pies("Azor", 10)
reks = Pies("Reksio",85)

print(azor)
print(isinstance(azor, Pies))
print(isinstance(azor, object))
print(dir(azor))

azor.waga = 10
azor.waga += 1
print(azor.waga)

print(azor == reks)
print(azor, reks)

reks.szczekaj()
Pies.szczekaj(azor)

print(reks.ile)