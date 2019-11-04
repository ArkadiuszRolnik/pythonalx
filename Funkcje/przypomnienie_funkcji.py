def do_potęgi (podstawa, wykladnik): # nawiasy są obowiązkowe, mogą być puste
    return podstawa ** wykladnik

#użycie

wynik = do_potęgi(2,12)
wynik2 = do_potęgi(5,5)

print(wynik)

def unique_letters(text):
    u_letters = set (text)
    u_letters = "".join(u_letters)
    return u_letters, len(text)

dane = unique_letters("Rafał Korzeniewski")
print(dane)

print("litery: ", dane[0])