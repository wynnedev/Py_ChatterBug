import socket
import threading
import sys

class Client:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.client_socket.connect(("127.0.0.1", 8888))

        # create thread for client send message
        client_thread = threading.Thread(target = self.sendMessage)

        # daemon = true background close with application
        client_thread.daemon = True
        client_thread.start()

        while True:
            data = self.client_socket.recv(1024)

            if not data:
                break
                print("Connection Broken...")

            print(data.decode('utf-8'))

    def sendMessage(self):
        while True:
            self.client_socket.send(bytes(input(""), 'utf-8'))


client = Client()
