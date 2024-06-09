import socket

new_socket = socket.socket()
new_socket.bind(("0.0.0.0",50001))
new_socket.listen(4)
conn, addr = new_socket.accept()

new_socket.close()

# zeby sprawdzic polaczenie uruchom netcata:
# nc -v 127.0.0.1 50001