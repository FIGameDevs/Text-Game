class Connected:
    def __init__(self, client):  # TODO: Add character for this connection
        self.client = client


players = {}


def add_connection(client):
    if id(client) in players:
        print("Duplicitous id connected, what the hell? ", id(client))
        return
    print(client)
    players[id(client)] = Connected(client)


def remove_connection(client):
    if id(client) in players:
        players.pop(id(client))
