from ..Core import game
import pickle
import os


def save_world():
    if game.world is None:
        return
    for file_name in os.listdir("Game State/"):
        os.rename(file_name, file_name + "_old")
    with open("Game State/world.save", "wb") as f:
        pickle.dump(game.world, f)


def load_world():
    if game.world is not None:
        print("A world is already loaded, will not override.")
        return
    with open("Game State/world.save", "rb") as f:
        game.world = pickle.load(f)
