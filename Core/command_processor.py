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


prepositions_to = ["to", "toward", "into", "facing", "via", "towards"]
prepositions_by = ["by", "via", "using", "with", "through", "supported by", "next", "next to"]
prepositions_near = ["close", "near", "nearby", "at", "next", "next to"]
prepositions_at = ["at", "appearing in", "near to", "near", "on", "toward", "towards", "placed at", "by", "found in",
                   "along", "next to", "next"]
prepositions_in = ["in", "at", "by", "into", "inside", "within", "during"]
prepositions_on = ["on", "in", "at", "above", "beside", "near", "next", "next to", "on top of", "upon", "situated on"]
prepositions_for = ["as", "for", "because", "as long as", "since", "whereas", "to", "via", "towards"]
