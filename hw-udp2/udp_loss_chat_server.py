from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)
    while True:
        # 소켓의 블로킹 모드 timeout 설정
        # None인 경우, 무한정 블로킹됨
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break
    
    # 사용자로부터 메시지 입력 받음
    msg = input('-> ')
    reTx = 0
    while reTx <= 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)
        # 소켓의 timeout 설정. 해당 timeout 내 메시지
        # 수신을 못하면 timeout 예외 발생
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
