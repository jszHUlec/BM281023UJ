# npaisz program, ktory pobiera od uzytkownika wiek
# jesli uzytkownik pelnoletni to wyswietlamy komunikat
# 'dzien dobry panu'
# jezeli uzytkownik niepelnoletni to wysweitlmy 'czesc mlody'

wiek = int(input("podaj swoj wiek:"))

if wiek <= 0 :
    print("nieprawidlowe dane")
elif wiek >= 18:
    print ("dzien dobry panu")
else :
    print("czesc mlody")