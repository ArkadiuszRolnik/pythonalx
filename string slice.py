s = "Hello!"
print(s[0:5]) #od indeksu 0 do 4 włącznie
print(s[-3]) #3ci znak od końca

s = "Ruda tańczy jak szalona"
arr = s.split(" ")
print(arr)
print(arr[0]) #pierwszy element listy

print(s[0:16:2]) #co 2gi znak od indeksu 0 do 15 włącznie
print(s[::3]) #cały string co 3ci znak

#Grande-finale
#reverse w pythonie

print(s[::-1])

print("Hello"+"World!")

a="Hello"
b="ALX"

print(f"{a} {b}                   {1+2}")
print("{} {}    {}".format(a,b,5+7))

x = input("Podaj wartość x") #input zwraca zawsze napis, trzeba zmienić na int
print(x, type(x))

x = int(input("Podaj wartość x"))
print(x, type(x))

