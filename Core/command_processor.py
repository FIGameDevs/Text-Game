from .connected_players import Connected
import threading
import collections

comm_lock = threading.Lock()
comm_queue = collections.deque()

def enque(connected, command):
    comm_lock.acquire()
    comm_queue.append((connected, command))
    comm_lock.release()

def process():
    comm_lock.acquire()
    while len(comm_queue) > 0:
        conn, command = comm_queue.pop()
        print(command)
        conn.client.send(command.encode("utf-8", "backslashreplace"))
        pass
    comm_lock.release()


prepositions_to=["to","toward","into","facing","via","towards"]
prepositions_by=["by","via","using","with","through","supported by"]
prepositions_near=["close","near","nearby",]