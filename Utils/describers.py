class Material:
    __slots__ = ["KEY", "name", "color", "texture", "smell", "taste", "density", "hardness", "is_reflective",
                 "is_transparent"]
    mats = {}

    def __new__(cls, *args, **kwargs):
        instance = super(Material, cls).__new__(cls)
        instance.__init__(*args, **kwargs)
        if kwargs["KEY"] in Material.mats:
            print("!!!Material with same KEY already present, overriding!")
        Material.mats[kwargs["KEY"]] = instance

    def __init__(self, KEY: str, name: str = "thing", color: str = "colorless", texture: str = "flat",
                 smell: str = "nothing",
                 taste: str = "without taste", density: int = 50, hardness: int = 50, is_reflective: bool = False,
                 is_transparent: bool = False):
        self.name = name
        self.color = color
        self.texture = texture
        self.smell = smell
        self.taste = taste
        self.density = density
        self.hardness = hardness
        self.is_reflective = is_reflective
        self.is_transparent = is_transparent

    @classmethod
    def get(cls, key):
        return Material.mats[key]

    def describe(self, detail=0):
        if detail == 0:
            return self.name
        if detail == 1:
            return self.color + ' ' + self.name
        return self.texture + ' ' + self.color + ' ' + self.name


class State:
    __slots__ = ["wear", "filth"]
    wear_desc = ["factory new", "kinda new", "damaged", "totally broken"]  # TODO redo by somebody with language skills
    filth_desc = ["clean as fuck", "clean", "in dirt covered", "in dirt and poop covered"]

    def __init__(self, wear: int = 20, filth: int = 20):
        self.wear = wear
        self.filth = filth

    def is_interesting(self):
        return self.wear > 80 or self.wear < 20 or self.filth > 80 or self.filth < 20

    def describe(self, detail=0):
        if detail == 0:
            return ""
        wr = State.wear_desc[int((self.wear / 100) * (len(State.wear_desc) - 1))]
        fl = State.filth_desc[int((self.filth / 100) * (len(State.filth_desc) - 1))]
        if detail == 1:
            if self.wear < self.filth:
                if self.wear < 20:
                    return wr
                return fl
            else:
                if self.filth < 20:
                    return fl
                return wr
        if self.filth - self.wear > 50:
            return wr + ", but " + fl
        if self.wear - self.filth > 50:
            return wr + ", but still " + fl
        return wr + " " + fl


class Part:
    __slots__ = ["material", "state"]

    def __init__(self, material: Material, state: State):  # TODO implement shape etc..
        self.material = material
        self.state = state

    def describe(self, detail=0):
        if detail == 0:
            return self.material.describe(detail)
        if detail == 1:
            if self.state.is_interesting():
                return self.state.describe(detail) + " " + self.material.describe(0)
            else:
                return self.material.describe(detail)
        return self.state.describe(round(detail / 2)) + " " + self.material.describe(round((detail - 0.001) / 2))


class Description:
    def __init__(self, description: str, parts: tuple):
        self.description = description
        self.parts = parts

    def describe(self):
        text = self.description
        for i in range(len(self.parts)):
            while True:
                id = -1
                id_end = -1
                try:
                    id = text.index('%' + str(i))
                    id_end = text.index('%', id + 1)
                except ValueError:
                    break
                if id != -1:
                    num_index = id + len('%' + str(i)) + 1
                    num_id = int(text[num_index])
                    if id_end != num_index + 1:
                        print("Description detail must be one digit number!")
                        break
                    text = text.replace('%' + str(i) + "," + str(num_id) + '%', self.parts[i].describe(num_id))
        return text

from ..Utils import material_definitions
