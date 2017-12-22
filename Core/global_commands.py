from .connected_players import Connected
from Game.Core.Entities.player import Character
from ..Utils.vectors import Vec3
from .game import this_game


def get_globals():
    return globals()


def login(conn: Connected, name: str):
    if name[0] == "admin":
        conn.send_string("And what is your secret signing?\n")
        return password
    if name[0] == "exit":
        return True
    return False


def password(conn: Connected, pw: str):
    if pw[0] == "admin":
        conn.set_character(Character("Admin", Vec3(0.5, 1.85, 0.5), Vec3(0, 0, 0), None, conn.send_string))
        conn.character.send("Welcome to the game " + conn.character.name + "!")
        this_game.world.grid.add(conn.character)
        return True


def cmd_log_in(conn: Connected):
    conn.send_string("What is your name, adventurer?\n")
    conn.set_question(login)
