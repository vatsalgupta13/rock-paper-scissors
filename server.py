import socket
import random

host = '127.0.0.1'
port = 14900
Max_Connections = 5
missed = 0
secret = ""
turns = 5

def win(word, input):
    if input.lower() == "r" and word.lower() == "p":
        return "you lose"
    elif input.lower() == "r" and word.lower() == "s":
        return "you win"
    elif input.lower() == "p" and word.lower() == "s":
        return "you lose"
    elif input.lower() == "p" and word.lower() == "r":
        return "you win"
    elif input.lower() == "s" and word.lower() == "r":
        return "you lose"
    elif input.lower() == "s" and word.lower() == "p":
        return "you win"
    else:
        return "draw"


try:
    srv_sock = socket.socket()  # creates a socket
    print("The socket is created!")
except Exception as e:
    print("Socket creation error: ", e)

try:
    srv_sock.bind(("localhost", port))
    print("The socket is connected by host: ", host, " port: ", port)
except Exception as e:
    print("Socket configuration error: ", e)
    # while True:

srv_sock.listen(Max_Connections)
conn, addr = srv_sock.accept()
print("Successful connection: " + str(addr))


print("Welcome to Rock Paper Scissors. \nEnter r or p or s to play")
guess = str(conn.recv(1024).decode())
data = input("Input: ")
def correct_input(inp):
        if inp.lower() not in ["r","p","s"]:
            print("Incorrect Input")
            data1 = input("Input: ")
            correct_input(data1)
        pass
correct_input(data)
message = win(guess,data)
print(f"{data} vs {guess}")
print(message)
if message == "you win":
    conn.send(f"{guess} vs {data}\nyou lose".encode())
else:
    conn.send(f"{guess} vs {data}\nyou win".encode())
while True:
    guess = str(conn.recv(1024).decode())
    data = input("Input: ")
    def correct_input(inp):
        if inp.lower() not in ["r","p","s"]:
            print("Incorrect Input")
            data1 = input("Input: ")
            correct_input(data1)
        pass
    correct_input(data)
    message = win(guess, data)
    print(f"{data} vs {guess}")
    print(message)
    if message == "you win":
        conn.send(f"{guess} vs {data}\nyou lose".encode())
    else:
        conn.send(f"{guess} vs {data}\nyou win".encode())







