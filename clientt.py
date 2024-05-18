import socket

# 서버 설정
HOST = '192.168.0.18'  # 서버의 IP 주소
PORT = 8887  # 서버와 동일한 포트 번호

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 서버에 연결
    client_socket.connect((HOST, PORT))
    print('서버에 연결되었습니다.')

    while True:
        # 서버로부터 데이터 수신
        data_from_server = client_socket.recv(1024).decode()
        if data_from_server:
            print('서버로부터 데이터를 수신하였습니다:', data_from_server)
            # 필요한 작업 수행
except Exception as e:
    print('에러 발생:', e)
finally:
    # 연결 종료
    client_socket.close()
