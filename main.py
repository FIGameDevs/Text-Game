from .Core.entity import Entity, Material
from .Utils.vectors import Vec3
from .Utils.grid import Grid
from .Utils.random import Rand
from .Utils.English import dictionary
"""
tup = (1, 1, 2)

print(Vec3(*tup).magnitude())

grid = Grid()

grid.add(Entity("Dog", Vec3(0, 2.5, 0)))
grid.add(Entity("Car", Vec3(10, 0, 3)))
grid.add(Entity("Cat", Vec3(-10, 1, 40.22)))
grid.add(Entity("Giraffe", Vec3(1, 5, 0)))
grid.add(Entity("Plane", Vec3(12, 10, 30)))
grid.add(Entity("House", Vec3(22, 2, 20)))
grid.add(Entity("Pea", Vec3(-50, 0, 60)))

for item in grid.get_chunks(Vec3(-5, 1, 62), 100):
    print(item)

grid.print_chunks(Vec3(0, 0, 0), 100)


stone = Material(name="brick", color=("salmon-meat colored", "reddish"), shape=("square",),
                 begin=("masterfully cut", "well made"), end=None, age=None, texture=("rough", "hard"))

for i in range(10):
    print(stone.describe(2))
"""