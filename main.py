import threading
import queue
import socket
from .Core import command_processor
from .Core import connected_players

stop_server = False


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        threading.Thread(target=self.listen).start()

    def listen(self):
        global stop_server
        self.sock.listen(5)
        self.sock.setblocking(False)
        while not stop_server:
            client, address = None, None
            try:
                client, address = self.sock.accept()
            except:
                continue
            print(client)
            client.settimeout(240)  # TODO: Change client timeout
            connected_players.add_connection(client)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()
        print("Stopped listening.")

    def listenToClient(self, client, address):
        size = 1024
        global stop_server
        while not stop_server:
            try:
                data = client.recv(size)
                if data:
                    print(data.decode())
                    response = data
                    client.send(response)
                """
                else:
                    print("Client disconnected.")
                    connected_players.remove_connection(client)
                    client.close()
                    return True"""
            except:
                print("Error while serving client.", id(client))
                connected_players.remove_connection(client)
                client.close()
                return False
        connected_players.remove_connection(id(client))
        try:
            client.close()
        except:
            pass


def get_input_blocking():
    input_queue = queue.Queue()
    input_thread = threading.Thread(target=add_input, args=(input_queue,))
    input_thread.daemon = True
    input_thread.start()

    print("Waiting for input...")

    while not stop_server:
        if not input_queue.empty():
            process_input(input_queue.get())

    print("Stopped waiting for input.")


def stop():
    print("--Stopping server.--")
    global stop_server
    stop_server = True


def add_input(input_queue):
    global stop_server
    while not stop_server:
        inp = input()
        input_queue.put(inp)


def process_input(inp):
    inp = inp.lower()
    if inp == "quit" or inp == "q":
        stop()
    else:
        print("Input:", inp)  # TODO: process server commands


def main():
    print("Server starting. To quit type q.")

    server = ThreadedServer(" ", 2222)

    get_input_blocking()
    print("Server stopped.")


if __name__ == "__main__":
    main()
else:
    print("This should be main script!!!")
