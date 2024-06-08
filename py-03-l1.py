# pobierz od uzytkownika liczba przebiegow petli
# wyswietl wszsytkie przebiegi

# od uzytkownika: 4
# 0, 1, 2, 3, 4

od_uzytkownika = int(input("podaj liczba przebiegow petli:"))
for x in range(od_uzytkownika):
    print(x, end=', ')