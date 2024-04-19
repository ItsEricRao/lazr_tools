import socket
HOST = "127.0.0.1"
PORT = 7000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    print("[Lazr] Server Started.")
    with conn:
        print(f"[+] {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)