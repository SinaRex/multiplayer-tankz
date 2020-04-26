import socket

HOST = "127.0.0.1"
PORT = 40477


def main():
    # setup a listening socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Listening on %s:%d" % (HOST, PORT))

        connection, address = s.accept()
        with connection:
            print("Connection established: ", address)
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                print("Received: ", str(data))
                connection.send(b"okay")


if __name__ == "__main__":
    main()
