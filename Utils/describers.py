class Material:
    __slots__ = ["name", "color", "texture", "smell", "taste", "density", "hardness", "is_reflective", "is_transparent"]

    def __init__(self, name: str = "thing", color: str = "colorless", texture: str = "flat", smell: str = "nothing",
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
    def __init__(self, material: Material, state: State, shape: str = "shapeless"):  # TODO implement shape etc..
        self.material = material
        self.state = state

    def describe(self, detail=0):
        return self.state.describe(detail) + " " + self.material.describe(detail)


class Description:
    def __init__(self, description: str, parts: tuple):
        self.description = description
        self.parts = parts

    def describe(self):
        text = self.description
        for i in range(len(self.parts)):
            text = text.replace('%' + str(i) + '%', self.parts[i].describe(2))
        return text


mat = Material("stone", "dark-red", "rough", "wet concrete", "tasteless", 50, 50, False, False)
st = State(5, 70)
part = Part(mat, st)
desc = Description("This is a %0%!!!", (part,))
print(desc.describe())
