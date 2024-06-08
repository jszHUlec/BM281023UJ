# [ [1 .. 11],[1..11], [1..11] ]
# robimy liste klas o roznym rozmiarze, i przechowujemy w tablicy zagniezdzonej


tablica = []
ilosc_klas = int(input("ilosc klas?: "))
for x in range(ilosc_klas):
    tablica.append([])
    dlugosc = int(input(f"podaj rozmiar tablicy w klasie {x+1}:"))
    for y in range(dlugosc):
        tablica[x].append(y+1)

print(tablica)