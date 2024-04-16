import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
   
   #이름 출력
    msg = client.recv(1024)
    print(msg.decode())


    #학번 보내기
    number = 20211517
    numberendian = number.to_bytes(4, byteorder = 'little')
    client.send(numberendian)
    
    client.close()

