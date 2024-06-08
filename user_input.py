imie = "Jakub"
nazwisko = input("Podaj nazwisko: ")
print("Czesc" + " " + imie + " " + nazwisko) #https://www.w3schools.com/python/gloss_python_escape_characters.asp
print("Czesc", imie, nazwisko)
print(f"Czesc {imie} {nazwisko}")
print("Czesc %s %s" % (imie, nazwisko) ) # https://www.geeksforgeeks.org/python-output-formatting/
print("Czesc {} {}".format(imie, nazwisko)) #https://www.w3schools.com/python/ref_string_format.asp