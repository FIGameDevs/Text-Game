from Game.Core.Entities.entity import Container


class Game:
    def __init__(self):
        self.world = None
        self.data = None

    def initiate(self, world: Container, data: dict):
        self.world = world
        self.data = data

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        return None

    def __setitem__(self, key, value):
        if key in self.data:
            print("SECURITY: Can't override an already stored data container!")
            return
        self.data[key] = value


this_game = Game()


def update(time_delta):
    pass
