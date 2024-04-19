import socket

HOST = "127.0.0.1"
PORT = 7000

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        text = input("> ")
        s.sendall(bytes(text, 'utf-8'))
        data = s.recv(1024)

    print(f"[Server] {data!r}")