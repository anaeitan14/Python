import socket

DESTINATION_ADDRESS = ("localhost", 8050)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(DESTINATION_ADDRESS)

user_input = ""

while user_input != "EXIT":
    user_input = input("Enter your command: ")
    sock.sendall(user_input.encode())
    data = sock.recv(1024)

    print(data.decode())

sock.close()


