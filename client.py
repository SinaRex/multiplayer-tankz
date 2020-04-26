import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 40477


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(b"I want to play Tankz")
        data = s.recv(1024)
    print("received", str(data))


if __name__ == '__main__':
    main()
