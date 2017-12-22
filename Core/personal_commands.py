from Game.Core.Entities.player import Character


def cmd_brush(character: Character):
    character.add_xp("swag", 5)
    character.send("You brushed your hair and look way cooler now. At least you think so.")
