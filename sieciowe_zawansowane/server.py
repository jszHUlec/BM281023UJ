import socket
import time
import sieci

new_socket = socket.socket()
new_socket.bind(("0.0.0.0",50000))
new_socket.listen(4)
conn, addr = new_socket.accept()

sieci.czytaj_bufor(conn)
time.sleep(1)
conn.send("Jest OK".encode())
sieci.czytaj_bufor(conn)

new_socket.close()

