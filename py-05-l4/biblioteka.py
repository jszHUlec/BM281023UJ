import py_05_l4
def wyswietl():
    print("biblioteka.py", __name__)

def test():
    print("testy biblioteki")

if __name__ == '__main__':
    test()
    wyswietl()
    py_05_l4.wyswietl()