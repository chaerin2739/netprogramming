import socket
import threading

def handler(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
        except:
            break
    sock.close()

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(svr_addr)

my_id = input('ID를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

try:
    while True:
        msg = '[' + my_id + '] ' + input()
        sock.send(msg.encode())
except KeyboardInterrupt:
    print("연결을 종료합니다.")
finally:
    sock.close()
