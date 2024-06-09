import socket
import time
import sieci
new_socket = socket.socket()
new_socket.connect(("127.0.0.1", 50000))
time.sleep(5)

new_socket.send("Hello World".encode("UTF-8"))
new_socket.send(b"\nJak leci?")

time.sleep(5)

sieci.czytaj_bufor(new_socket)

new_socket.close()
