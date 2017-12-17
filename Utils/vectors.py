from cmath import sqrt


class Vec3:
    """
    Holds 3D coordinates and provides methods for manipulation.
    """
    __slots__ = ["x", "y", "z"]

    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.z = args[2]

    def __repr__(self):
        return "Vec3(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)

    def __lt__(self, other):
        return NotImplemented

    def __le__(self, other):
        return NotImplemented

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __gt__(self, other):
        return NotImplemented

    def __ge__(self, other):
        return NotImplemented

    def __hash__(self):
        return int(1009 + 100003 * self.x + 571871 * self.y + 936007 * self.z)

    def __dir__(self):
        return [self.x, self.y, self.z]

    def __len__(self, other):
        return 3

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return Vec3(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        return Vec3(self.x // other, self.y // other, self.z // other)

    def __mod__(self, other):
        return Vec3(self.x % other, self.y % other, self.z % other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        self.z //= other
        return self

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __invert__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def sqr_magnitude(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def magnitude(self):
        return sqrt(self.sqr_magnitude())


class Vec2:
    """
    Holds 2D coordinates and provides methods for manipulation.
    """
    __slots__ = ["x", "y"]

    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]

    def __repr__(self):
        return "Vec2(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)

    def __lt__(self, other):
        return NotImplemented

    def __le__(self, other):
        return NotImplemented

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __gt__(self, other):
        return NotImplemented

    def __ge__(self, other):
        return NotImplemented

    def __hash__(self):
        return int(1009 + 100003 * self.x + 571871 * self.y)

    def __dir__(self):
        return [self.x, self.y]

    def __len__(self, other):
        return 2

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec3(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vec3(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Vec3(self.x // other, self.y // other)

    def __mod__(self, other):
        return Vec3(self.x % other, self.y % other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self

    def __neg__(self):
        return Vec3(-self.x, -self.y)

    def __invert__(self):
        return Vec3(-self.x, -self.y)

    def sqr_magnitude(self):
        return self.x * self.x + self.y * self.y

    def magnitude(self):
        return sqrt(self.sqr_magnitude())
