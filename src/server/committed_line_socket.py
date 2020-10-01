import socket
import pickle


class CommittedLineSocket:
    def __init__(self):
        self.host = '127.0.0.1'  # The server's hostname or IP address
        self.port = 8080  # The port used by the server
        self.to_add = []

    def accept(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            client_connection, client_address = s.accept()
            with client_connection:
                print('Connected by', client_address)
                while True:
                    data = client_connection.recv(1024)
                    if not data:
                        break
                    decoded = pickle.loads(data)
                    self.to_add.append(decoded)


if __name__ == "__main__":
    connection = CommittedLineSocket()
