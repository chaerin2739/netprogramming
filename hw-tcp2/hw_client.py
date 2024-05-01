import socket

HOST = 'localhost'
PORT = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    expression = input("Enter calculation: ")
    if expression.lower() == 'q':
        s.sendall(expression.encode())
        break

    s.sendall(expression.encode())
    while True:
        data = s.recv(1024)
        if not data:
            break
        print("Result:", data.decode())

s.close()
print("Calculator closed.")
