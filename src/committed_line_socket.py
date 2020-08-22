import socket
import pickle


class CommittedLineSocket:
    def __init__(self):
        self.host = '127.0.0.1'  # The server's hostname or IP address
        self.port = 8080  # The port used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                completed = False
                while not completed:
                    data = conn.recv(1024)
                    decoded = pickle.loads(data)
                    print(str(decoded))
                    completed = True





