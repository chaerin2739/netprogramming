import socket
import select
import time

def broadcast_message(sender_socket, message, clients):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                client_socket.close()
                clients.remove(client_socket)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 3000))
server_socket.listen(5)
server_socket.setblocking(False)

clients = []

print('Server Started')

try:
    while True:
        readable, _, exceptional = select.select([server_socket] + clients, [], clients)
        
        for s in readable:
            if s is server_socket:
                client_socket, addr = server_socket.accept()
                clients.append(client_socket)
                print('new client', addr)
            else:
                try:
                    data = s.recv(1024)
                    if data:
                        message = data.decode()
                        addr = s.getpeername()
                        if 'quit' in message:
                            print(addr, 'exited')
                            s.close()
                            clients.remove(s)
                        else:
                            print(time.asctime() + str(addr) + ':' + message)
                            broadcast_message(s, data, clients)
                    else:
                        addr = s.getpeername()
                        print(addr, 'disconnected')
                        s.close()
                        clients.remove(s)
                except:
                    addr = s.getpeername()
                    print(addr, 'disconnected')
                    s.close()
                    clients.remove(s)
        
        for s in exceptional:
            addr = s.getpeername()
            print(addr, 'disconnected')
            s.close()
            clients.remove(s)

except KeyboardInterrupt:
    print("서버를 종료합니다.")
finally:
    server_socket.close()
