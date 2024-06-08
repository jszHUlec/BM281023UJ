# popros uzytkownika o przygotowanie slownika
# z list uslug i portami na ktorych dzialaja
# jak chcesz skonczyc wpisywanie to wpisz 'EXIT'

# 1. - wprowadz nowa wartosc
# 2. - wyswietl zawartosc slownika
# exit - wyjscie z programu
slownik = {}
while True:
    print("")
    print("1. - wprowadz nowa wartosc")
    print("2. - wyswietl slwonik")
    print("exit - wyjdz z programu")

    komenda = input("podaj komende z menu: ").strip().upper()

    if komenda == "1":
        usluga = input("Podaj nazwe uslugi:").upper()
        port = int(input("Podaj numer portu:").strip())
        slownik[usluga] = port
    elif komenda == "2":
        print("slownik: ",slownik)
    elif komenda == "EXIT":
        break
    else:
        print("bledna komenda. Sprobuj ponownie")

input("Koniec programu. Wcisnij entern, zeby zamknac")