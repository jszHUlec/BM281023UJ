import socket
import biblioteka
import base64

new_socket = socket.socket()
new_socket.bind(("0.0.0.0",50001))
new_socket.listen(4)
conn, addr = new_socket.accept()

while True:
    otrzymane = base64.b64decode(biblioteka.czytaj_bufor(conn)).decode()
    print(otrzymane)
    if "exit" == otrzymane:
        break
    message = input("wyslij do klienta: ")
    #conn.send(message.encode())
    conn.send(base64.b64encode(message.encode()))
    if message.strip().lower() == "exit":
        break


new_socket.close()

