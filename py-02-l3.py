# mamy mozliwosc zdobycia 100 punktow
# 0-19 - > 1 < 20
# 20 - 39 -> 2 >= 20
# 40 - 59 -> 3
# 60 - 79 -> 4
# 80 - 99 > 5
# 100 -> 6
# napisz program, ktory po wprowadzeniu ilosci punktow wygeneruje ocene z testu

punkty = int(input("Podaj liczbe punktow: "))
ocena = ""
if punkty >= 0 and punkty < 20 : # True / False
    ocena = 1
elif punkty >= 20 and punkty < 40 :
    ocena = 2
elif punkty >= 40 and punkty < 60:
    ocena = 3
elif punkty >= 60 and punkty < 80:
    ocena = 4
elif 80 >= punkty < 100:
    ocena = 5
else:
    ocena = 6


print("ocena koncowa to: ", ocena)