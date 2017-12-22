from .connected_players import Connected
from ..Utils.English import dictionary, keyword_dictionary
from ..Core import parsing
import threading
import collections


def tokenize(input_text: str, connected: Connected):
    quote_parts = input_text.strip().split('"')
    words = []
    for i in range(len(quote_parts)):
        if i % 2 == 0:
            words += quote_parts[i].strip("?!.").split()
        else:
            words.append('"' + quote_parts[i] + '"')
    lookup(words, connected)


def lookup(inp_words: list, connected: Connected):
    if connected.has_question():
        if not connected.answer_question(inp_words):
            connected.send_string("Your answer doesn't make sense to me, please try again.\n")
        return
    for word in inp_words:
        if word[0] == '"':
            continue
        if not keyword_dictionary.is_keyword(word):
            if not dictionary.is_in_dictionary(word):
                connected.send_string(
                    "Sorry, I don't know what '" + word + "' means, did you mean " + dictionary.get_closest_word_baseonly(
                        word) + "? If you want to say something literally, use " + '"quotes"\n')
                return
    parse(inp_words, connected)


def parse(inp_words: list, connected: Connected):
    parsing.start_parse(inp_words, connected)
    connected.send_string("Dummy parsed.")
    pass


def bind():
    pass


comm_lock = threading.Lock()
comm_queue = collections.deque()


def enqueue(connected, command):
    comm_lock.acquire()
    comm_queue.append((connected, command))
    comm_lock.release()


def process():
    comm_lock.acquire()
    while len(comm_queue) > 0:
        conn, command = comm_queue.pop()
        tokenize(command, conn)
        # conn.client.send(command.encode("utf-8", "backslashreplace"))
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
