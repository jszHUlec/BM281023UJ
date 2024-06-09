import socket
import time

def czytaj_bufor(conection):
    while True:
        data = conection.recv(10).decode("UTF-8")
        print(data)
        if len(data) < 10:
            print("---koniec---")
            break

new_socket = socket.socket()
new_socket.bind(("0.0.0.0",50000))
new_socket.listen(4)
conn, addr = new_socket.accept()

czytaj_bufor(conn)


time.sleep(1)
conn.send("Jest OK".encode())

new_socket.close()

