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
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                completed = False

                while not completed:
                    data = conn.recv(1024)
                    if data:
                        decoded = pickle.loads(data)
                        print(decoded)
                        for item in decoded:
                            self.to_add.append(item)


if __name__ == "__main__":
    connection = CommittedLineSocket()


