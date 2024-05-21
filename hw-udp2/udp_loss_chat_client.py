from socket import *
import time

SERVER_IP = '127.0.0.1'  # 서버 IP 주소
PORT = 3333
BUFF_SIZE = 1024


sock = socket(AF_INET, SOCK_DGRAM)
server_address = (SERVER_IP, PORT)

while True:
    message = input("-> ")
    if message.lower() == "exit":
        break
    
    # 메시지 전송 및 재전송
    reTx = 0
    while reTx <= 5:
        msg_with_retry = f"{reTx} {message}"
        sock.sendto(msg_with_retry.encode(), server_address)
        sock.settimeout(2)
        
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
            if data.decode() == 'ack':
                break
        except timeout:
            reTx += 1
            continue
    else:
        continue

    # 서버의 응답 수신
    try:
        sock.settimeout(None)
        data, addr = sock.recvfrom(BUFF_SIZE)
        sock.sendto(b'ack', addr)
        print("<-", data.decode())
    except timeout:
        pass

sock.close()
