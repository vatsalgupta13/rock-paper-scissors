import socket

host = '127.0.0.1'
port = 14900

cli_sock = socket.socket()
cli_sock.connect(("localhost", port))


print("Welcome to Rock Paper Scissors. \nEnter r or p or s to play")
data = input("Input: ")
def correct_input(inp):
        if inp.lower() not in ["r","p","s"]:
            print("Incorrect Input")
            data1 = input("Input: ")
            correct_input(data1)
        pass
correct_input(data)
cli_sock.send(str(data).encode())
print(cli_sock.recv(1024).decode())
#word = cli_sock.recv(1024).decode()
while True:
    data = input("Input: ")
    def correct_input(inp):
        if inp.lower() not in ["r","p","s"]:
            print("Incorrect Input")
            data1 = input("Input: ")
            correct_input(data1)
        pass
    correct_input(data)
    cli_sock.send(str(data).encode())
    print(cli_sock.recv(1024).decode())


cli_sock.close()
