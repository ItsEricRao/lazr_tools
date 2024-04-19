import socket
import threading
text_type = "utf-8"

server_ip = "127.0.0.1"
port  = 7000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server_ip,port))

#This function gets other clients messages, so any client has access to all messages
def messages():
    while True:
        try:
            message = client.recv(1024).decode(text_type)
            print(message)
        except:
            print("ERROR")
            client.close()
            break

#This function waits for the user input(message)
def write():
    while True:
        text = str(input("> "))
        client.send(text.encode(text_type))


receive_thread = threading.Thread(target=messages)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
