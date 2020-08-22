import socket
import pickle


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)


class CommittedServerSocket:
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
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





