import socket
import time
new_socket = socket.socket()
new_socket.connect(("127.0.0.1", 50001))

time.sleep(5)
new_socket.close()