lista = [1, 0, 10, 'a']

for i in lista:
    try:
        print(10 / i)
    except ZeroDivisionError:
        print("Dzielisz przez zero")
    except TypeError:
        print("Dzielisz przez coś co nie jest liczbą")
    except:
        pass


# CTRL + ALT + L Poprawia stylistykę kodu