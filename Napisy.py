#
#Typ danych: napisy (albo string)
#
napis1 = "Ala ma kota"
napis2 = 'Ala ma kota'
napis3 = 'A to jest "cudzysłów"'
napis4 = "A to jest \"cudzysłów\" "

#dlugosc = len(napis1)
#print("Długość zmiennej napis1 to", dlugosc, "znaków")

#wiek = input("Podaj wiek:")
#print("Twój wiek to",wiek.strip())
s = "Ruda tańczy jak szalona"
print(s.capitalize()) #kapitalki
print(s.upper()) #w górę
print(s.lower()) #w dół
print(s.title()) #formatowanie jako tytuł
print(s.swapcase()) #duże->małe, małe->duże
print(s.center(100)) #centrowanie
print(s.replace("R","D")) #zamiana znaków
print("Czy liczba:",s.isdecimal()) #sprawdzenie czy string jest liczbą

print("4-ta litera:", s[3]) #pobierz 4ta literę napisu, pierwsza to 0
print("Litera przedostatnia:", s[-2]) #pobierz przedostatnią literę, ostatnia to -1
s = "Hello!"
print(s[0:5])