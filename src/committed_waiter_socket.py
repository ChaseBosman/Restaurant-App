import socket
import pickle


class CommittedWaiterSocket:
    def __init__(self, data, port=8080):
        self.host = '127.0.0.1'  # The server's hostname or IP address
        self.port = port  # The port used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as open_socket:
            open_socket.connect((self.host, self.port))
            print(data)
            encoded = pickle.dumps(data)
            open_socket.sendall(encoded)

