"""
Napisz program, ktory pobiera od uzytkownika
nazwe i sciezke pliku do skopiowania
i kopiuje je w podane miejsce z nowa nazwa
"""

import os
cel = input("Podaj plik do skopiowania")
zrodlo = input("Podaj plik docelowy")
os.system(f"cp {cel} {zrodlo}")