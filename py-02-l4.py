uslugi = {"FTP":21, "HTTP":[80,8080], "HTTPS":443, "SSH":22}

# napisz program, ktory sprawdza na jakim porcie dziala usluga ?
print("dostepne uslugi:",uslugi.keys())
                        # "ftp" -> "FTP" -> 'od_uzytkownika'

od_uzytkownika = input("podaj usluge, ktora chcesz sprawdzic: ").strip().upper()
if od_uzytkownika in uslugi.keys(): # TRUE
    print(uslugi[ od_uzytkownika ])
else: #FALSE
    print("brak uslugi")
