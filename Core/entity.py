from ..Utils.grid import Grid
from ..Utils.random import Rand


class Entity:  # TODO: Add relations like "on the table", "behind the dresser"
    """
    Base class for all ingame objects.
    """

    def __init__(self, name, pos, size):
        """

        :string name: Object name
        :Vec3 pos: World position of object
        """
        self.name = name
        self.__position = pos
        self.__size = size
        self.containing_grid = None

    def __repr__(self):
        return str(self.name) + " in " + str(self.containing_grid) + " at position: " + str(self.__position)

    def move_to(self, pos):
        if self.containing_grid is not None:
            self.containing_grid.update_position(self, pos)

        self.__position = pos

    def move_by(self, vector):
        if self.containing_grid is not None:
            self.containing_grid.update_position(self, self.__position + vector)
        self.__position += vector

    def position(self):
        return self.__position

    def size(self):
        return self.__size

    def bounds(self):
        """
        Returns tuple of two Vec3s, lower and upper bound of entity
        :return: (Vec3, Vec3)
        """
        return self.__position - self.__size / 2, self.__position + self.__size / 2

    def is_in_bounds(self, pos):
        """
        Returns whether pos is inside of entity's bounds
        :param pos:
        :return:
        """
        lower, upper = self.bounds()
        return lower.x < pos.x < upper.x and lower.y < pos.y < upper.y and lower.z < pos.z < upper.z


class Container:
    def __init__(self, chunk_size):
        self.grid = Grid(chunk_size)


class Material:
    __slots__ = ["name", "color", "shape", "age", "texture", "density", "hardness", "reflective", "transparent",
                 "begin", "end", "smell", "taste", "whole_desc", "rand"]

    def __init__(self, name: str = "object", color: tuple = ("colorless", "grey"), shape: tuple = ("shapeless",),
                 begin: tuple = None, end: tuple = None,
                 age: tuple = None,
                 texture: tuple = None, smell: tuple = ("odorless",), taste: tuple = ("tasteless", "without taste"),
                 density: int = 50,
                 hardness: int = 50, reflective: bool = False, transparent: bool = False) -> None:
        """
        :param color: string tuple, color adjectives
        :param shape: string tuple, shape adjectives
        :param age: string tuple, age adjectives
        :param texture: string tuple, texture adjectives
        :param density: number 1-100 used in simulation
        :param hardness: number 1-100 used in simulation
        :param reflective: bool, affects description
        :param transparent: bool, allows looking inside object
        """
        self.rand = Rand()
        self.name = name
        self.color = color
        self.shape = shape
        self.age = age
        self.texture = texture
        self.begin = begin
        self.end = end
        self.density = density
        self.hardness = hardness
        self.reflective = reflective
        self.transparent = transparent
        self.smell = smell
        self.taste = taste
        self.whole_desc = []
        if begin is not None:
            self.whole_desc.append(begin)
        if shape is not None:
            self.whole_desc.append(shape)
        if age is not None:
            self.whole_desc.append(age)
        if color is not None:
            self.whole_desc.append(color)
        if texture is not None:
            self.whole_desc.append(texture)

    def describe(self, detail=0):
        """
        Returns material description.
        :param detail: 0 - only name, the higher the more adjectives
        :return:
        """
        text = ""
        lrange = min(detail, len(self.whole_desc))
        for i in range(lrange):
            category = self.whole_desc[self.rand.randint(int((i / lrange) * len(self.whole_desc)),
                                                         int(((i + 1) / lrange) * (len(self.whole_desc) - 1)))]
            text += category[self.rand.randint(0, len(category) - 1)] + " "
        text += self.name
        return text


class Parts:
    __slots__ = ["materials", "relations"]

    def __init__(self, materials, relations):
        """

        :param materials: tuple of materials
        :param relations: tuple of strings, they will be zipped before and after material descs
        """
        self.materials = materials
        self.relations = relations

    def describe(self, detail=0):
        print("TODO")  # TODO: zip relations and materials
