"""
Tworzenie rekordu pracownika
2 parametry obowiazkowe, 2 opcjonalne
Ma zwrócić zmienną typu słownik
"""

def utworz_pracownika(imie,nazwisko, email='info@firma.pl', telefon=None):
    pracownik = dict()
    pracownik["imie"] = imie
    pracownik["nazwisko"] = nazwisko
    pracownik["email"] = email
    pracownik["telefon"] = telefon
    return pracownik

print(utworz_pracownika("Jan", "Kowalski"))
print(utworz_pracownika("Adam", "Nowak", "anowak@firma.pl", "345345345"))
print(utworz_pracownika("Jan", "Zielinski", telefon="98234789"))
print(utworz_pracownika("Jan", "Zielinski", email="jzielinski@firma.pl"))
print(utworz_pracownika("Jan", "Zielinski", "jzielinski@firma.pl"))