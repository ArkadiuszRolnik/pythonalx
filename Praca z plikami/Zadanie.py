# 1)Napisz funkcję która otworzy podany jako argument plik (podana nazwa pliku) i wypisze go numerując linię

# jeśli w pliku txt

# Plik.txt
#Raz
#Dwa
#Trzy


# 2) pozwól na uruchomienie go z command line

import sys

file_name = sys.argv[1]

def otwieranie(nazwa):
    with open(nazwa) as f:

        for i, line in enumerate(f, start=1):
            print(i, line.rstrip())

otwieranie(file_name)



