from .entity import Entity


class Creature(Entity):
    def __init__(self, name: str, pos, size, limbs : list):
        super().__init__(name, pos, size)
        self.limbs = limbs


class Limb:
    def __init__(self, name, hp, importance, description):
        self.name = name
        self.hp = hp
        self.importance = importance
        self.description = description

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
        self.description.describe()