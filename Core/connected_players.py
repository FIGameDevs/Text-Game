from .player import Character


class Connected:
    def __init__(self, client):  # TODO: Add character for this connection
        self.client = client
        self.character = None

    def set_char(self, character: Character):
        self.character = character

    def send_string(self, text):
        self.client.send(text.encode())


players = {}


def add_connection(client):
    if id(client) in players:
        print("Duplicitous id connected, what the hell? ", id(client))
        return
    players[id(client)] = Connected(client)


def remove_connection(client):
    if id(client) in players:
        players.pop(id(client))


def get_connected(client):
    if id(client) in players:
        return players[id(client)]


def send_message(client, text):
    if id(client) in players:
        players[id(client)].client.send(text.encode())


def send_to_all(text):
    for k, v in players.items():
        v.client.send(text.encode())


def yield_sockets():
    for k, v in players.items():
        yield v.client
