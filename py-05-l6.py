""" napisz funkcje rekurencyjna, ktora wysweitla zagniezdzona liste"""
lista = [1,2,"a",[4,5,"b",6], [7,[8,"d",9]]]
def drukuj_liste(lst):
    for element in lst:
        print(element)
        if type(element) == list:
            drukuj_liste(element)

drukuj_liste(lista)