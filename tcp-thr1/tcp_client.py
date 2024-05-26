import socket
import threading

def receive_handler(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            print(msg)
        except ConnectionError:
            print("서버와의 연결이 종료되었습니다.")
            break

def main():
    server_address = ('localhost', 2500)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 서버에 연결
    client_socket.connect(server_address)

    my_id = input('ID를 입력하세요: ')
    client_socket.send(('[' + my_id + ']').encode())

    # 메시지 수신을 담당하는 스레드 시작
    receive_thread = threading.Thread(target=receive_handler, args=(client_socket,))
    receive_thread.daemon = True
    receive_thread.start()

    # 메시지 전송
    while True:
        msg = '[' + my_id + '] ' + input()
        client_socket.send(msg.encode())

if __name__ == "__main__":
    main()
