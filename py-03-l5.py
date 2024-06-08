# zaimplementuj funkcjonalnosc sklepu
# robisz zakupy produktow ze zmiennej 'sklep'
# zakupy robisz do wysokosci budzetu
# po wybraniu produktu, produkt kopiowany jest do koszyka
# i wartosc odejmowana jest od budzetu
budzet = 50
koszyk = []
sklep = {"jablka":10, "sliwki":15, "mleko":5}

print("Witamy w sklepie")
print("dostepne produkty to:",sklep)

while True:
    print("twoj budzet to: ",budzet)
    print("obecny koszyk to: ",koszyk)
    produkt = input("podaj nazwe produktu: ").strip().lower()
    if "exit" == produkt:
        break
    if produkt in sklep:
        if budzet - sklep[produkt] >= 0:
            budzet = budzet - sklep[produkt]  # jablko, sliwka, mleko
            koszyk.append(produkt)
        else:
            print("brak srodkow na zakup produktu")
    else:
        print("blednie wybrany produkt. Sprobuj ponwonie!")

print("**** podsumowanie ****")
print("twoj budzet to: ",budzet)
print("obecny koszyk to: ",koszyk)
