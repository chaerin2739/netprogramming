import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    while True:
        try:
            message = input('Enter command ("send mboxID message" or "receive mboxID"): ')
            client_socket.sendto(message.encode(), server_address)

            if message == "quit":
                break

            response, _ = client_socket.recvfrom(1024)
            print( response.decode())

        except Exception as e:
            print(f"Error: {e}")

    client_socket.close()

if __name__ == "__main__":
    run_client()
