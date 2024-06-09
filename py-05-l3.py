"""
stworz funkcje, ktora zmienia wartosc zmiennej globalnej
"""

text = "hello world"

def zmiana():
    text = "nowy tekst"
    return text

text = zmiana()
print(text)