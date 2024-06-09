"""
Napisz program, ktory sprawdza czy zgadles wylosowana liczbe
"""

import random
wylosowana = random.randint(0,10)
# print(wylosowana)

def pobierzLiczbe(numer):
    while True:
        try:
            return int(input(f"podaj {numer} wartosc"))
        except:
            print("to nie liczba")

# popros uzytkownika o podanie liczby i sprawdz czy == wylosowana
licznik = 0
while True:
    liczba = pobierzLiczbe("1")
    licznik = licznik+1
    if liczba == wylosowana:
        print("Gratulacje!!!! Zgadles liczbe")
        print("potrzebowales ",licznik,"prob")
        break