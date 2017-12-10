from ..Utils.vectors import Vec3


class ExactGrid:
    __slots__ = ["chunks", "chunk_size"]

    def __init__(self, chunk_size=16):
        self.chunk_size = chunk_size
        self.chunks = {}

    def __setitem__(self, pos, item):
        ch_pos = pos // self.chunk_size
        inch_pos = pos % self.chunk_size
        if ch_pos not in self.chunks:
            self.chunks[ch_pos] = {}
        if inch_pos not in self.chunks[ch_pos]:
            self.chunks[ch_pos][inch_pos] = []
        self.chunks[ch_pos][inch_pos].append(item)

    def __getitem__(self, pos):
        ch_pos = pos // self.chunk_size
        inch_pos = pos % self.chunk_size
        if ch_pos not in self.chunks:
            return []
        if inch_pos not in self.chunks[ch_pos]:
            return []
        return self.chunks[ch_pos][inch_pos]

    def remove_item(self, pos, item):
        ch_pos = pos // self.chunk_size
        inch_pos = pos % self.chunk_size
        if ch_pos not in self.chunks:
            return False
        if inch_pos not in self.chunks[ch_pos]:
            return False
        try:
            self.chunks[ch_pos][inch_pos].remove(item)
        except ValueError:
            return False
        return True

    def remove_item_global(self, item):
        for k, v in self.chunks.items():
            for kk, vv in v.items():
                try:
                    vv.remove(item)
                    return
                except ValueError:
                    pass


class Grid:
    """
    Holds Entities in chunks.
    """
    __slots__ = ["chunks", "chunk_size"]

    def __init__(self, chunk_size=16):
        self.chunk_size = chunk_size
        self.chunks = {}

    def add(self, entity):
        """
        Adds an Entity into the grid
        :param entity: Entity instance
        """
        ch_pos = entity.position() // self.chunk_size
        if ch_pos not in self.chunks:
            self.chunks[ch_pos] = []
        entity.containing_grid = self
        self.chunks[ch_pos].append(entity)

    def get_chunk(self, pos):
        ch_pos = pos // self.chunk_size
        if ch_pos not in self.chunks:
            self.chunks[ch_pos] = []
        return self.chunks[ch_pos]

    def get_chunks(self, pos, distance):
        """
        Yields chunks around a point.
        :param pos: World position around which to yield
        :param distance: World distance to which to yield
        :return: Yields lists of Entities
        """
        ch_pos = pos // self.chunk_size
        ch_dist = distance // self.chunk_size

        for x in range(ch_pos.x - ch_dist, ch_pos.x + ch_dist + 1):
            for y in range(ch_pos.y - ch_dist, ch_pos.y + ch_dist + 1):
                for z in range(ch_pos.z - ch_dist, ch_pos.z + ch_dist + 1):
                    new_pos = Vec3(x, y, z)
                    if new_pos not in self.chunks:
                        continue
                    yield self.chunks[new_pos]

    def print_chunks(self, pos, distance):
        """
        Prints a horizontal slice
        :param pos:
        :param distance:
        :return:
        """
        ch_pos = pos // self.chunk_size
        ch_dist = distance // self.chunk_size

        for x in range(ch_pos.x - ch_dist, ch_pos.x + ch_dist + 1):
            for z in range(ch_pos.z - ch_dist, ch_pos.z + ch_dist + 1):
                new_pos = Vec3(x, ch_pos.y, z)
                if new_pos not in self.chunks:
                    print("|_|", end="")
                else:
                    print("|X|", end="")
            print()

    def remove(self, entity):
        """
        Removes Entity instance from the grid.
        :param entity: The entity to remove.
        :return: True if entity was found and removed, else False.
        """
        ch_pos = entity.position() // self.chunk_size
        entity.containing_grid = None
        if ch_pos not in self.chunks:
            self.chunks[ch_pos] = []
        try:
            self.chunks[ch_pos].remove(entity)
        except ValueError:
            return False
        return True

    def update_position(self, entity, new_pos):
        old_ch_pos = entity.position() // self.chunk_size
        new_ch_pos = new_pos // self.chunk_size
        if old_ch_pos != new_ch_pos:
            self.remove(entity)
            self.add(entity)

    def __str__(self):
        return "Grid-" + str(id(self))
