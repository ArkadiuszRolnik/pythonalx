#zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu
#lata przestępne(1990,2020)
#[1992, 1996, 2000, 2004, 2008, 2016, 2020)
# rok przestępny jest co (4 lata, o ile nie dzieli się


def test_lata_przestepne():
    assert lata_przestepne(2020, 2030) == [2020, 2024, 2028]