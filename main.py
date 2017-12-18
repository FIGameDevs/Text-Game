import threading
import queue
import socket
import time
from .Core import command_processor
from .Core import connected_players
from .Core import game
from .Utils import persistence


def testing():
    return


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
            print("Client", id(client), "connected.")
            client.settimeout(240)
            client.daemon = True
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
                    command_processor.enqueue(connected_players.get_connected(client),
                                              data.decode("utf-8", "backslashreplace").strip())
                """
                else:
                    print("Client disconnected.")
                    connected_players.remove_connection(client)
                    client.close()
                    return True"""
            except socket.timeout:
                print("Client", id(client), "timed out.")
                connected_players.remove_connection(client)
                client.close()
                return False
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
    connected_players.send_to_all("---Server is closing---")
    for client in connected_players.yield_sockets():
        client.close()
    global stop_server
    stop_server = True


def add_input(input_queue):
    global stop_server
    while not stop_server:
        inp = input()
        input_queue.put(inp)


def process_input(inp):
    if inp == "":
        return
    inp = inp.lower()
    if inp == "quit" or inp == "q":
        stop()
    elif inp == "save":
        persistence.save_world()
    elif inp == "load":
        persistence.load_world()
    elif inp[0] == "/":
        command_processor.enqueue(None, inp[1:])
    else:
        print("Input:", inp)  # TODO: process server commands


def main():
    print("Server starting. To quit type q.")

    server = ThreadedServer(" ", 2222)

    threading.Thread(target=get_input_blocking).start()
    testing()  # for tests
    current_time = time.time()
    while not stop_server:
        command_processor.process()
        delta = time.time() - current_time
        game.update(delta)
        current_time = time.time()

    print("Server stopped.")


if __name__ == "__main__":
    main()
else:
    print("This should be main script!!!")
