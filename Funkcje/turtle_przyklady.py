import turtle

"""
napisz funkcję która narysuje dowolny wielokąt foremny


"""

print(help(turtle))

def wielokat(n):

    for i in range(n):

        turtle.right(360/n) #skręca w prawo o zadany kąt
        turtle.forward(300/n) # idzie do przodu ileś tam kroków

    turtle.done()

wielokat(100)
