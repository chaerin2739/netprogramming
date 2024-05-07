import socket
import mimetypes

def parse_request_line(request_line):
    parts = request_line.split()
    if len(parts) >= 2:
        return parts[1]
    return None

def get_mime_type(filename):
    mime_type, _ = mimetypes.guess_type(filename)
    return mime_type

def run_web_server(host='', port=80):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)

        print(f"웹 서버가 {port} 포트에서 시작되었습니다...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"클라이언트 {client_address}가 연결되었습니다.")

            with client_socket:
                request_line = client_socket.recv(1024).decode()
                print("Received request line:", request_line)

                filename = parse_request_line(request_line)
                if filename:
                    filename = filename.lstrip("/")
                    print("Requested file:", filename)

                    try:
                        if filename == 'index.html':
                            f = open(filename, 'r', encoding='utf-8')
                            mime_type = 'text/html'
                            data = f.read()
                            f.close()
                            response = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n{data}"
                            client_socket.sendall(response.encode('utf-8'))
                        elif filename == 'iot.png':
                            f = open(filename, 'rb')
                            mime_type = 'image/png'
                            data = f.read()
                            f.close()
                            response = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n".encode() + data
                            client_socket.sendall(response)
                        elif filename == 'favicon.ico':
                            f = open(filename, 'rb')
                            mime_type = 'image/x-icon'
                            data = f.read()
                            f.close()
                            response = f"HTTP/1.1 200 OK\r\nContent-Type: {mime_type}\r\n\r\n".encode() + data
                            client_socket.sendall(response)
                        else:
                            raise FileNotFoundError()

                    except FileNotFoundError:
                        error_message = "<HTML><HEAD><TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"
                        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: " + str(len(error_message)) + "\r\n\r\n" + error_message
                        client_socket.sendall(response.encode('utf-8'))

                else:
                    print("Invalid request")

if __name__ == "__main__":
    run_web_server()
