"""
Zrob petle for dla 4 krokow
pobierz od uzytkwonika liczby
obsluz bledy w aplikacji
"""

for i in range(4): # 0, 1, 2, 3
    try:
        x = int(input(f"podaj {i} liczbe"))
        print("podales liczbe:",x)
    except ValueError:
        print("nastepnym razem podaj liczba!")

print("koniec programu")
