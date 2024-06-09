def czytaj_bufor(conection):
    odczytane = ""
    while True:
        data = conection.recv(30).decode("UTF-8")
        odczytane = odczytane + data
        if len(data) < 30:
            return odczytane