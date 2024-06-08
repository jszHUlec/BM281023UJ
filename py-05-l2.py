"""
napisz kilka funkcji zwracajacych rozne typy danych
i sprawdz jakego typu dane sa zwracane
"""

x1="jeden"
x2="dwa"

# krotka, lista, slownik, int, float, boolean
def zwraca_krotke():
    return (x1,x2)
def zwraca_liste():
    return [x1,x2]
def zwraca_slownik():
    return {x1:x2}
def zwraca_int():
    return 3
def zwraca_float():
    return 3.5
def zwraca_boolean():
    return False

print(type(zwraca_krotke()), zwraca_krotke())
print(type(zwraca_liste()), zwraca_liste())
print(type(zwraca_slownik()), zwraca_slownik())
print(type(zwraca_int()), zwraca_int())
print(type(zwraca_float()), zwraca_float())
print(type(zwraca_boolean()), zwraca_boolean())
