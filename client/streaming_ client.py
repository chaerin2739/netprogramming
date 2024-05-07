import socket
import cv2
import numpy as np

BUF_SIZE = 8192  # 버퍼 사이즈 정의
LENGTH = 10  # 프레임 길이 정보를 위한 문자열 길이

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP/IP 소켓 생성
sock.connect(('localhost', 5000))  # 서버에 연결

while True:
    sock.send(b'start')  # 서버에 시작 신호 전송
    
    rx_size = 0  # 수신된 데이터 크기
    data = b''  # 수신 데이터
    while rx_size < LENGTH:  # 프레임 길이 정보를 받을 때까지 반복
        rx_buf = sock.recv(BUF_SIZE)  # 데이터 수신
        if not rx_buf:
            break
        data += rx_buf
        rx_size += len(rx_buf)
        
    if rx_size < LENGTH:  # 프레임 길이 정보를 제대로 받지 못한 경우 종료
        break
    
    frame_len = int(data)  # 프레임 길이 정보를 정수로 변환
    sock.send(b'image')  # 이미지 데이터를 요청하는 신호 전송
    
    rx_size = 0
    byteData = b''
    while rx_size < frame_len:  # 프레임 길이만큼의 데이터를 받을 때까지 반복
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break
        byteData += rx_buf
        rx_size += len(rx_buf)
        
    if rx_size < frame_len:  # 프레임 데이터를 제대로 받지 못한 경우 종료
        break
    
    data = np.frombuffer(byteData, dtype='uint8')  # 바이트 데이터를 NumPy 배열로 변환
    imgDecode = cv2.imdecode(data, 1)  # 이미지 디코드
    cv2.imshow('image', imgDecode)  # 이미지 표시
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키를 누르면 반복 종료
        break

sock.close()  # 소켓 닫기