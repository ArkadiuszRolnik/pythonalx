#zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu
#lata przestępne(1990,2020)
#[1992, 1996, 2000, 2004, 2008, 2016, 2020)
# rok przestępny jest co (4 lata, o ile nie dzieli się przez 100, ale może być podzielna przez 400)

def czy_przestepny(rok):

        return rok%4 == 0 and (rok%100 != 0 or rok%400 == 0) # skrotowa forma zamiast if bo to i tak przyjmuje tylko True albo False

def lata_przestepne(rok_od, rok_do):
    if rok_od>rok_do:
        return None

    lata = list() # pusta lista
    for rok in range (rok_od, rok_do+1):
        if czy_przestepny(rok):
            lata.append(rok)
    return lata

#print (lata_przestepne(2020,2030))


def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]