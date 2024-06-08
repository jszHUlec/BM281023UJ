"""
pobierz od uzytkownika tekst zakodowany base64
i odczytac jego tresc
"""

import base64
msg = input("Podaj zaszyfrowany kod:")
print(base64.b64decode(msg))

msg = input("Podaj tekst do zaszyfrowania:")
print(base64.b64encode(msg.encode("UTF-8")))

