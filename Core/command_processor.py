from .connected_players import Connected
import threading
import collections

comm_lock = threading.Lock()
comm_queue = collections.deque()

