"""
pobierz od uzytkownika sciezke do pliku
i wysweitl jego zawartosc
"""
sciezka = input("podaj sciezke do pliku: ")

with open(sciezka,"r") as plik:
    x = 0
    for linijka in plik.readlines():
        print(f"{x}:",linijka, end="")
        x=x+1
