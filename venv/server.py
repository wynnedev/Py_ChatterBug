import socket
import threading
import sys

class Server:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    def __init__(self):
        self.server_socket.bind(('0.0.0.0', 8888))
        self.server_socket.listen(1)

    def handler(self, conn, addr):
        while True:
            data = "ChatterBug " + str(addr[1])
            data += " says: "
            message = conn.recv(1024)
            data += message.decode('ascii')
            data_out = data.encode('utf-8')

            for connection in self.connections:
                connection.send(data_out)

            if not data:
                print(str(addr[1]))
                break

    def run(self):
        while True:
            conn, addr = self.server_socket.accept()
            message = "Connected...You are Chatterbug " + str(addr[1])
            conn.send(message.encode('utf-8'))
            server_thread = threading.Thread( target=self.handler, args=(conn,addr))
            server_thread.daemon = True
            server_thread.start()
            self.connections.append(conn)

            print(self.connections)

server = Server()
server.run()