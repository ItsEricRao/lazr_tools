import pydirectinput, ctypes, os, threading, psutil, time, socket, keyboard, base64, zlib, tempfile
from tkinter import *
SendInput = ctypes.windll.user32.SendInput

'''
Global Variables
'''
# adaptive dpi
ctypes.windll.shcore.SetProcessDpiAwareness(1)
# get factor of the device
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
# set pydirectinput module time interval between presses
pydirectinput.PAUSE = 0
# set GTAV process name.
PROCNAME = "GTA5.exe"
# network block status
block_stat = False

# tcp server variables
text_type = "utf-8"
server_ip = "127.0.0.1"
port  = 7000
msg = ""

# favicon
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

'''
HotKey Detection
'''
def key_detect():
    keyboard.add_hotkey('f3', lambda: snack())
    keyboard.add_hotkey('f4', lambda: armor())
    keyboard.add_hotkey('f5', lambda: mechanic())
    keyboard.add_hotkey('f6', lambda: lester())
    keyboard.add_hotkey('f9', lambda: write())
    keyboard.add_hotkey('f12', lambda: unblock())
    keyboard.add_hotkey('f11', lambda: block())
    keyboard.wait()

'''
Init
'''
os.system('netsh advfirewall firewall delete rule name="GTAOL"')

'''
GUI
'''
class GUI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        global entry, stat
        self.root = Tk()
        # set program zoom
        self.root.call('tk', 'scaling', ScaleFactor/60)
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.title("Lazr Tools")
        # text labels
        title = Label(self.root, text="IP地址", font=("Microsoft YaHei", 7))
        text = Label(self.root, text="F3 快速零食\nF4 快速防弹衣\nF5 快速叫技工\nF6 快速叫莱斯特\nF9 集体杀进程\nF11 进程断网\nF12 进程断网恢复", font=("Microsoft YaHei", 10), justify='left') 
        btn = Button(self.root, text="连接", font=("Microsoft YaHei", 7), command=conn)
        stat = Label(self.root, text="未连接", font=("Microsoft YaHei", 7))
        entry = Entry(self.root)

        title.grid(row=0, sticky=E)
        entry.grid(row=0, column=1)
        btn.grid(row=0, column=2)
        text.grid(row=1,column=1)
        stat.grid(row=2,column=2,sticky=E)
        self.root.resizable(False,False)
        self.root.iconbitmap(default=ICON_PATH)
        self.root.mainloop()

gui = GUI()

'''
TCP Client
'''
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def messages():
    global msg
    while True:
        msg = client.recv(1024).decode(text_type)

def write():
    text = "kill"
    client.send(text.encode(text_type))

def detect():
    global msg, stat
    while msg != "ready":
        time.sleep(0.05)
    stat.config(text="已连接")
    while msg != "kill":
        time.sleep(0.05)
    kill()

def conn():
    global server_ip, receive_thread, detect_thread
    server_ip = str(entry.get())
    client.connect((server_ip,port))
    receive_thread.start()
    detect_thread.start()

'''
Threads
'''
detect_thread = threading.Thread(target=detect, daemon=True)
receive_thread = threading.Thread(target=messages, daemon=True)
key_thread = threading.Thread(target=key_detect, daemon=True)
key_thread.start()

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

'''
Macro
'''
# Quick Snack
def snack():
    print("LOG >> KeyPressed F3 -> QuickSnack")
    pydirectinput.press('m')
    pydirectinput.press('down', presses=3)
    pydirectinput.press('enter')
    pydirectinput.press('down', presses=5)
    pydirectinput.press('enter')
    time.sleep(0.1)

# Quick Armor
def armor():
    print("LOG >> KeyPressed F4 -> QuickArmor")
    pydirectinput.press('m')
    pydirectinput.press('down', presses=3)
    pydirectinput.press('enter')
    pydirectinput.press('down', presses=4)
    pydirectinput.press('enter')
    pydirectinput.press('up', presses=3)
    time.sleep(0.1)

# Quick Mechanic
def mechanic():
    print("LOG >> KeyPressed F5 -> QuickMechanic")
    pydirectinput.press('up')
    time.sleep(0.5)
    pydirectinput.press('up')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('enter')
    time.sleep(0.4)
    pydirectinput.press('space')
    time.sleep(0.5)
    pydirectinput.press('right', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('up')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down')
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('down')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('up')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('space')
    time.sleep(0.1)

# Quick Lester
def lester():
    print("LOG >> KeyPressed F6 -> QuickLester")
    pydirectinput.press('up')
    time.sleep(0.5)
    pydirectinput.press('up')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('enter')
    time.sleep(0.4)
    pydirectinput.press('space')
    time.sleep(0.5)
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('right')
    pydirectinput.press('down')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down', presses=2)
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down')
    pydirectinput.press('left')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('up')
    pydirectinput.press('right')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('down')
    pydirectinput.press('enter')
    time.sleep(0.1)
    pydirectinput.press('space')
    time.sleep(0.1)
    


