import przyklad
def wyswietl():
    print("biblioteka.py", __name__)

def test():
    print("testy biblioteki")

if __name__ == '__main__':
    test()
    wyswietl()
    przyklad.wyswietl()