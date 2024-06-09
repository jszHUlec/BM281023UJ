import socket
import time
import biblioteka
import base64

new_socket = socket.socket()
new_socket.connect(("127.0.0.1", 50001))
time.sleep(1)

while True:
    message = input("wiadomosc do serwera: ")
    new_socket.send(base64.b64encode(message.encode()))
    if message.strip().lower() == "exit":
        break

    otrzymane = base64.b64decode(biblioteka.czytaj_bufor(new_socket)).decode()
    print(otrzymane)
    if otrzymane == "exit":
        break

new_socket.close()
