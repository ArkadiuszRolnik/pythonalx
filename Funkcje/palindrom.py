#napisz funkcję, która sprawdzi czy dany tekst jest palindromem

#is_palindrom("kajak") is True
#is_palindrom("kot") is False

def is_palindrom(text):
    text = text.lower().replace(" ","").replace(".","").replace(",","")
    if text == text[::-1]:
        return True
    else:
        return False

def test_is_palindrom_for_palindrom():
    assert is_palindrom("kajak") is True
    assert is_palindrom("Kajak") is True
    assert is_palindrom("A to idiota") is True
    assert is_palindrom("A to idiota.") is True
    assert is_palindrom("Ada, gmina za nim gada.") is True
"""
inna wersja
def is_palindrom(text):
    text = text.lower()
    signs_to_remove = " .,;?"
    for s in signs_to_remove:
        text = text.replace(s, "")
    return text == text[::-1]:
"""