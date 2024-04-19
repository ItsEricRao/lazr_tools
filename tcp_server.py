import threading
import socket

text_type = "utf-8"
host = "0.0.0.0"
port = 7000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)

clients = []

def broadcast(msg):
    for i in clients:
        message = msg.encode(text_type)
        i.send(message)

def get_message(client_reference):
    while True:
        try:

            message = client_reference.recv(1024).decode(text_type)
            broadcast(message)

        except:

            index = clients.index(client_reference)
            clients.remove(client_reference)
            client_reference.close()
            break

def new_client():
    while True:

        client_reference,client_info = server.accept()

        print(f"Connected with {client_info}")

        clients.append(client_reference)
        client_reference.send(str("ready").encode(text_type))
       
        thread = threading.Thread(target=get_message, args=[client_reference])
        thread.start()


new_client()