from ..Utils.grid import Grid


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
