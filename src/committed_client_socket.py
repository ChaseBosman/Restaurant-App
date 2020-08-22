import socket
import pickle

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080  # The port used by the server


class CommittedClientSocket:
    def __init__(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as open_socket:
            open_socket.connect((HOST, PORT))
            print(data)
            encoded = pickle.dumps(data)
            open_socket.sendall(encoded)

