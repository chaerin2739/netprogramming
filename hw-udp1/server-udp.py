import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print("UDP server up and listening")

    mbox = {}

    while True:
        try:
            message, client_address = server_socket.recvfrom(1024)
            message = message.decode()
            print(f"Received message: {message}")

            if message.startswith("send "):
                parts = message.split(' ', 2)
                if len(parts) < 3:
                    continue
                mbox_id = parts[1]
                msg = parts[2]
                if mbox_id not in mbox:
                    mbox[mbox_id] = []
                mbox[mbox_id].append(msg)
                server_socket.sendto("OK".encode(), client_address)

            elif message.startswith("receive "):
                parts = message.split(' ', 1)
                if len(parts) < 2:
                    continue
                mbox_id = parts[1]
                if mbox_id in mbox and mbox[mbox_id]:
                    msg = mbox[mbox_id].pop(0)
                    server_socket.sendto(msg.encode(), client_address)
                else:
                    server_socket.sendto("No messages".encode(), client_address)

            elif message == "quit":
                break

        except Exception as e:
            print(f"Error: {e}")

    server_socket.close()
    print("Server shutdown")

if __name__ == "__main__":
    run_server()
