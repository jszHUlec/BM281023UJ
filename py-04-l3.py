"""
pobierz od uzytkownika tekst w petli while
zapisz te tekst do pliku example.txt
zakoncz dzialanie po wpisaniu exit
"""
try:
    file = open("example.txt","w")
    while True:
        message = input("Podaj linijke do dopisania: ")
        if "exit" == message.lower().strip():
            break
        file.write(message+"\n")
        file.flush()
except:
    print("blad w uruchomieniu programu")
finally:
    file.close()