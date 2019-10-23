#Zapytaj użytkownika o tekst
#Zapytaj o szerokość
#Wyświetl tekst który będzie miał same duże litery, tekst powinien być wycentrowany zgodnie z wartością szerokości

tekst = input("Podaj napis: ")
szerokosc = int(input("Podaj szerokość:"))
print("!"+ tekst.center(szerokosc) + "!")
print(f"!{tekst.center(szerokosc)}!")