f = open("tekst")
print(f)
f.close()

#ASCII
#a-z A-Z 0-9
#7 bit 128 możliwości
# 1111111 = 1 + 2 + 4 + 8 + 16 + 32 + 64

#Unicode
#Kodowanie UTF-8

f = open("tekst")
for line in f:
    print(line)
f.close()

try:
    f = open('tekst')
    # coś tu robimy
except Exception:
    print("Wyjątek")
finally:
    f.close()

with open("tekst", encoding="utf-8") as f:
    for l in f:
        print(f.read())



