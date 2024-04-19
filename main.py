import pydirectinput, ctypes, os, threading, psutil, time, socket
SendInput = ctypes.windll.user32.SendInput

'''
Global Variables
'''
# set pydirectinput module time interval between presses
pydirectinput.PAUSE = 0
# set GTAV process name.
PROCNAME = "mspaint.exe"
# network block status
block_stat = False

# tcp server variables
text_type = "utf-8"
server_ip = "127.0.0.1"
port  = 7000
msg = ""

'''
Init
'''
os.system('netsh advfirewall firewall delete rule name="GTAOL"')

'''
TCP Client
'''
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((server_ip,port))

def messages():
    global msg
    while True:
        msg = client.recv(1024).decode(text_type)

def write():
    text = "kill"
    client.send(text.encode(text_type))

def detect():
    global msg
    while msg != "kill":
        time.sleep(0.05)
    kill()

receive_thread = threading.Thread(target=messages)
receive_thread.start()
detect_thread = threading.Thread(target=detect)
detect_thread.start()

'''
Functions
'''
def kill():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()

def block():
    global block_stat
    os.system('netsh advfirewall firewall add rule name="GTAOL" protocol=UDP  dir=out localport=6672 action=block')
    time.sleep(0.1)
    block_stat = True

def unblock():
    global block_stat
    os.system('netsh advfirewall firewall delete rule name="GTAOL"')
    time.sleep(0.1)
    block_stat = False

