from .Core.entity import Entity
from .Utils.vectors import Vec3
from .Utils.grid import Grid
from .Utils.random import Rand
# from .Utils.English import dictionary #long load
from .Utils.describers import Material, State, Part, Description
# from .Utils.English import dictionary,pronunciation
from .Core.player import Character

import threading
import queue
import socket


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

        threading.Thread(target=self.listen).start()

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(300)  # TODO: Change client timeout
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    print(data.decode())
                    response = data
                    client.send(response)
                else:
                    print("Client disconnected.")
                    client.close()
                    return True
            except:
                client.close()
                return False


def get_input_blocking():
    input_queue = queue.Queue()
    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    print("Waiting for input...")

    while True:
        if not input_queue.empty():
            process_input(input_queue.get())


def add_input(input_queue):
    while True:
        inp = input()
        input_queue.put(inp)


def process_input(inp):
    print("Input:", inp)  # TODO: process server commands


def main():
    print("Server starting.")

    server = ThreadedServer(" ", 2222)

    get_input_blocking()




if __name__ == "__main__":
    main()
else:
    print("This should be main script!!!")
