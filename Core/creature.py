from .entity import Entity

class Creature(Entity):
    def __init__(self, name: str, pos, size, limbs: list):
        super().__init__(name, pos, size)
        self.limbs = limbs

    def add_limb(self, limb):
        self.limbs.append(limb)

    def del_limb(self, limb):
        self.limbs.remove(limb)


class Limb:
    def __init__(self, name, hp, importance, orientation, description):
        self.name = name
        self.hp = hp
        self.importance = importance
        self.description = description
        self.orientation = orientation

    def change_hp(self, hp):
        self.hp += hp
        if self.hp < 0:
            self.hp = 0

    def set_hp(self, hp):
        self.hp = hp
        if self.hp < 0:
            self.hp = 0

    def get_hp(self):
        return self.hp

    def is_dead(self):
        return self.hp == 0, self.importance

    def get_name(self):
        return self.name

    def describe(self):
        return self.description.describe()

    def is_orientation(self, orient):
        return orient & self.orientation == orient
        # TODO - OTESTOVAT :P