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


class Part:
    def __init__(self, material, shape, age):
        pass  # dodělat pro konkrétní item, tyhle hodnoty se mění - stáří, rozbitost..

    def describe(self, detail=0):
        return self.material.describe(detail)


class Description:
    def __init__(self, description: str, materials: tuple):
        self.description = description
        self.materials = materials

    def describe(self):
        text = self.description
        for i in range(len(self.materials)):
            text = text.replace('%' + str(i) + '%', self.materials[i].describe(1))
        return text


mat = Material("stone", "dark-red", "rough", "wet concrete", "tasteless", 50, 50, False, False)

desc = Description("This is a %0%!!!", (mat,))
print(desc.describe())
