"""

$ python czytaj_logi.py dane/input.txt

user-9: 3520 s
user-6: 2950 s

user-8;LOGIN;384

"""

with open("dane/logs.txt") as dane:
    for i in dane:
        print(i.split(";",2))
