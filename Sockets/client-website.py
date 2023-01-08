import socket

SERVER_ADDRESS = ("networks.cyber.org.il", 8820)
MESSAGE = "Testing sockets in Python"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(SERVER_ADDRESS)

sock.sendall(MESSAGE.encode())
replay = sock.recv(1024)

print(replay.decode())

sock.close()
