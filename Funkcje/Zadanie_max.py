#Napisz funkcje, ktora zwroci maksimum z 3 podanych liczb
#max_of_three(10, 1, 17) 17
#w celu rozwiazania mozna napisać więcej niż jedną funkcję

def max_of_two(x,y):
    if x > y:
        return x
    return y

def max_of_three(a, b, c):
    return max_of_two(max_of_two(a,b),c)

print(max_of_three(1,5,3))