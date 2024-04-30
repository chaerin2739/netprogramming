import socket
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Server is listening on port ', port)
    print('Connection from ', addr)
    massage = 'Yoo chae rin'
    client.send(massage.encode())

    msg = client.recv(1024)
    print('Received from client', msg.decode())

    client.close()

