import socket
import pickle

HEADER = 1024 # length of the message 
PORT = 5050
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))

def start():
    print(client.recv(HEADER).decode(FORMAT))
    connected = True
    while connected:
        msg = input() # waits for user input
        
        if msg == "d":
            send(DISCONNECT_MESSAGE)
            connected = False
        else:
            send(msg)

start()
# send(DISCONNECT_MESSAGE)
