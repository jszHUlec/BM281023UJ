"""
Napisz funkcje, ktora uruchamia sie,
tylko jezeli plik uruchomiony bezposrednio
"""
import biblioteka

def wyswietl():
    print("py_05_l4.py", __name__)

if __name__ == '__main__':
    print("Jestem w main!!!!")
    wyswietl()
    biblioteka.wyswietl()
