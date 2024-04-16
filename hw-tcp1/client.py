import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())


#이름 보내기
name = "Yoo Chae Rin"
sock.send(name.encode())

#학번 받기

numberendian = sock.recv(4)
number = int.from_bytes(numberendian, byteorder ='little')
print(number)


sock.close()