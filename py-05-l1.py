# TO JEST PLIK PYTHON DO ROZDZIALU 5
def pobierzLiczbe(numer):
    while True:
        try:
            return int(input(f"podaj {numer} wartosc"))
        except:
            print("to nie liczba")

def pobierzOperacje():
    while True:
        operacja = input("podaj operacje (+,-,*,/)")
        if operacja in ['+','-','*','/']:
            return operacja
        else:
            print("bledna operacja")

def dodawanie(num1, num2):
    print("rezultat dodawania: ", num1+num2)
def odejmowanie(num1, num2):
    print("rezultat odejmowania: ", num1-num2)
def mnozenie(num1, num2):
    print("rezultat mnozenia: ", num1 * num2)
def dzielenie(num1, num2):
    try:
        print("rezultat dzielenia: ", num1/num2)
    except ZeroDivisionError:
        print("Dzielenie przez 0. Operacja zabroniona")

def main():
    liczba1 = pobierzLiczbe('1')
    liczba2 = pobierzLiczbe('2')
    operacja = pobierzOperacje()

    if "+" == operacja:
        dodawanie(liczba1, liczba2)
    elif "-" == operacja:
        odejmowanie(liczba1, liczba2)
    elif "*" == operacja:
        mnozenie(liczba1, liczba2)
    elif "/" == operacja:
        dzielenie(liczba1, liczba2)

while True:
    main()

