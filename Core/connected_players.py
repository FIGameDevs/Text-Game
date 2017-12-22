from .player import Character

class ClientDummy:
    def __init__(self):
        pass

    def send(self, data):
        print(data.decode())

    def close(self):
        print("Tried closing a dummy client.")

class Connected:
    def __init__(self, client):  # TODO: Add character for this connection
        self.client = client
        self.character = None
        self.__question = None

    def set_character(self, character: Character):
        self.character = character

    def send_string(self, text):
        self.client.send(text.encode())

    def set_question(self, question):
        """
        Sets question func for the player to answer, for example Do you want to engage? Yes/No
        The question should return True if succeeded, False in case of bad input
        :param question:
        :return:
        """
        self.__question = question

    def has_question(self):
        return self.__question is not None

    def answer_question(self, answer: list):
        if self.__question is not None:
            res = self.__question(answer)
            if res:
                self.__question = None
                return True
            return False

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
