def czytaj_bufor(conection):
    while True:
        data = conection.recv(10).decode("UTF-8")
        print(data)
        if len(data) < 10:
            print("---koniec---")
            break