import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(('localhost', 80))

    while True:
        expression = input("Enter calculation: ")
        if expression.lower() == 'q':
            client_socket.sendall(expression.encode())
            break

        client_socket.sendall(expression.encode())
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Result:", data.decode())

print("Calculator closed.")
