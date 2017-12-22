from .vectors import Vec3

mats = {}


class Material:
    __slots__ = ["KEY", "name", "color", "texture", "smell", "taste", "density", "hardness", "is_reflective",
                 "is_transparent"]
    mats = {}
    """
    def __new__(cls, *args, **kwargs):
        instance = super(Material, cls).__new__(cls)
        instance.__init__(*args, **kwargs)
        if kwargs["KEY"] in Material.mats:
            print("!!!Material with same KEY already present, overriding!")
        Material.mats[kwargs["KEY"]] = instance
    """

    def __init__(self, KEY: str, name: str = "thing", color: str = "colorless", texture: str = "flat",
                 smell: str = "nothing",
                 taste: str = "without taste", density: int = 50, hardness: int = 50, is_reflective: bool = False,
                 is_transparent: bool = False):
        if KEY in mats:
            print("Material key already added, a mistake?")
        mats[KEY] = self
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
            return self.color
        return self.texture + ' ' + self.color


class State:
    __slots__ = ["wear", "filth", "size", "wear_desc", "filth_desc", "height_desc", "width_desc", "size_desc"]
    unnat_wear_desc = ["brand-new", "untouched", "new", "intact", "scratched", "damaged",
                       "broken"]  # TODO redo by somebody with language skills
    nat_wear_desc = ["untouched", "new", "intact", "scratched", "damaged", "broken"]  # TODO complete

    unnat_filth_desc = ["unbelievably clean", "spotless", "very clean", "pretty clean", "clean", "kinda clean",
                        "a little dusty", "unpolished", "dusty", "scruffy", "in dust covered", "uncleaned",
                        "little dirty", "kinda dirty", "pretty dirty", "messy", "decaying"]
    nat_filth_desc = ["untouched", "fresh", "neat", "nice", "greasy", "unsanitary", "ugly", "absolutely dirty"]

    n_height_desc = []  # TODO complete and include in describe()
    alive_height_desc = []

    n_width_desc = []
    alive_width_desc = []

    n_size_desc = []
    alive_size_desc = []

    def __init__(self, wear: int = 20, filth: int = 20, is_natural: bool = False, is_alive: bool = False,
                 size: Vec3 = Vec3(1, 1, 1)):
        self.wear = wear
        self.filth = filth
        self.size = size

        if is_natural:
            self.wear_desc = State.nat_wear_desc
            self.filth_desc = State.nat_filth_desc
        else:
            self.wear_desc = State.unnat_wear_desc
            self.filth_desc = State.unnat_filth_desc
        if is_alive:
            self.height_desc = State.alive_height_desc
            self.width_desc = State.alive_width_desc
            self.size_desc = State.alive_size_desc
        else:
            self.height_desc = State.n_height_desc
            self.width_desc = State.n_width_desc
            self.size_desc = State.n_size_desc

    def describe(self, detail=0):
        wr = self.wear_desc[int((self.wear / 100) * (len(self.wear_desc) - 1))]
        fl = self.filth_desc[int((self.filth / 100) * (len(self.filth_desc) - 1))]
        if detail == 0:
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
        return fl + " " + wr


class Part:
    __slots__ = ["material", "state", "name"]

    def __init__(self, material: Material, state: State, name: str = "item"):  # TODO implement shape etc..
        self.name = name
        self.material = material
        self.state = state

    def describe(self, detail=0):
        if detail == 0:
            return self.name
        if detail == 1:
            return self.state.describe(detail) + " " + self.name
        return self.state.describe(round(detail / 2)) + " " + self.material.describe(
            round((detail - 1.001) / 2)) + " " + self.name


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
