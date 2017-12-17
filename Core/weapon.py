from .entity import Entity
class Weapon(Entity):

    def __init__(self,damage,description,name,pos):
        self.damage=damage
        self.description=description
        super().__init__(name,pos)






