import socket
from datetime import datetime
from random import randint

listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("localhost", 8050)
listening_sock.bind(server_address)
listening_sock.listen(1)

client_sock, client_address = listening_sock.accept()

while True:
    client_msg = client_sock.recv(4).decode()

    match client_msg:
        case "TIME":
            time = datetime.now().strftime('%H:%M:%S')
            client_sock.sendall(time.encode())
        case "NAME":
            server_name = "Python server"
            client_sock.sendall(server_name.encode())
        case "RAND":
            num = str(randint(1,10))
            client_sock.sendall(num.encode())
        case "EXIT":
            client_sock.sendall("Connection closed".encode())
            client_sock.close()
            break

listening_sock.close()
