my_list = [1, "a", "ala", "kot", 121]
print(my_list)
print(my_list[0])

my_list2 = [1, 2, 3, my_list] #czyli [1, 2, 3, [1, "a", "ala", "kot", 121]]

print(my_list2[3][1]) #zagnieżdżenie

print(dir(my_list))

my_list.append(10) # dopisanie 10 na końcu

print(my_list)

print(my_list.pop()) #zrzucenie 1 elementu

print(my_list)

print(my_list.index("a")) # podaj indeks tego elementu

a = [1, 2, 3]
b = [3, 4, a]

print(a)
print(b)
a.append(10)
print(b)

a[0] = 100

print(a)

x = (1, 2, 3)
print(dir(x))
print(x[0])
y = (4, 5, 6)
x = x + y
print(1 in x)

