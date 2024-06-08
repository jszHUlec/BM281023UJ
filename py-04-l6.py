"""
stworz katalog lub plik w katalogu biezacym
w petli while przechodz pomiedzy katalogami
nazwa katalogu / pliku pobierana jest od uzytkownika
"""
import os, datetime

while True:
    try:
        print("jestes w katalogu:", os.getcwd())
        cmd = input(
            """MENU:
    wprowadz * zeby wyswietlic zawartosc katalogu
    wprowadz '1' zeby dodac katalog
    wprowadz '2' zeby stworzyc nowy plik
    wprowadz '3' zeby przejsc do innego katalogu\n""").strip().lower()
        if "exit" == cmd:
            break
        elif "*" == cmd:
            print(os.listdir())
        elif "1" == cmd:
            os.mkdir(input("Podaj nazwe katalogu")) # zastapic input()
        elif "2" == cmd:
            with open(input("Podaj nazwe pliku"),"w") as file: # input()
                file.write(str(datetime.datetime.now()))
        elif "3" == cmd:
            os.chdir(input("podaj katalog"))
        else:
            print("Bledny wybor")
    except:
        print("cos poszlo zle")