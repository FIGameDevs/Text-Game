from ..Core import game
import pickle
import os


def save_world():
    for file_name in os.listdir("Game State/"):
        os.rename(file_name, file_name + "_old")
    with open("Game State/world.save", "wb") as f:
        pickle.dump(game.this_game, f)
    print("Game world saved.")


def load_world():
    with open("Game State/world.save", "rb") as f:
        game.world = pickle.load(f)
    print("Game world loaded.")
