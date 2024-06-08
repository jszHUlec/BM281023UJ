# mamy liczbe np. 15
# popros uzytkownika o wpisanie liczby
# program sie konczy gdy wpisana liczba = 15
# wyswietl uzytkownikowi po ilu probach znalazl liczbe
import random
liczba = random.randint(0,20)
proba = 1

while 1==1:
    uzytkownik = int()
    if 0 == input("podaj liczbe"):
        break
    proba = proba + 1

print(f"zgadles po {proba} probach")