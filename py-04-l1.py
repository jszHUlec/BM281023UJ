"""
pobierz od uzytkownika liczbe i wykonaj dzielenie przez zero
dzielenie powinno byc w bloku try/except
jezeli bedzie blad ...to wyswietl prawidlowy komunikat
"""
while True:
    rezultat = 0
    try:
        x = int(input("Podaj pierwsza liczbe:"))
    except ZeroDivisionError:
        print("Blad dzielenia przez 0")
    except ValueError:
        print("Wpisz prawidlowa liczbe")
    else:
        print(rezultat)
        break

print("koniec programu")