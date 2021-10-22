import socket
import threading

HEADER = 1024 # length of the message 
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = "DISCONNECT"
KEY_LENGTHS = 16

# Creating socket with IPv4 addr
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# handles individual communication between client and server
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    conn.send("Quantum Key Exchange Program \n".encode(FORMAT))
    conn.send("------------------------------------\n".encode(FORMAT))
    conn.send("Enter a message\n".encode(FORMAT))
    conn.send("OR\n".encode(FORMAT))
    conn.send("Press 'd' to disconnect\n".encode(FORMAT))
    conn.send("------------------------------------\n".encode(FORMAT))


    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # reveieve a message from the client through the "conn" socket

        # if mes_length is not none (has a message)
        if msg_length:

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                conn.send("Connection Terminated!".encode(FORMAT))
                print(DISCONNECT_MESSAGE)
                connected = False
            else:
                print(f"[{addr}] {msg}")
                conn.send(f"Message Received".encode(FORMAT))

    conn.close()

# handles new connections with the server
def start():
    server.listen()

    print(f"[LISTENING] Server is listening on {SERVER}")
    # infinitely wait for a new client
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") # shows how many active clients are connected


print("[STARTING] server is starting...")
start()

