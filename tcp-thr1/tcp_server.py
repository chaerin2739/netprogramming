import socket
import threading
import time

clients = []

def client_handler(client_socket, addr):
    global clients
    clients.append((client_socket, addr))
    print('new client', addr)
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            if 'quit' in message:
                print(addr, 'exited')
                clients.remove((client_socket, addr))
                break
            print(time.asctime() + str(addr) + ':' + message)
            for client, client_addr in clients:
                if client_addr != addr:
                    client.send(data)
        except:
            break
    client_socket.close()
    clients.remove((client_socket, addr))
    print(addr, 'disconnected')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 2500))
server_socket.listen(5)

print('Server Started')

try:
    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=client_handler, args=(client_socket, addr))
        client_thread.daemon = True
        client_thread.start()
except KeyboardInterrupt:
    print("서버를 종료합니다.")
finally:
    server_socket.close()
