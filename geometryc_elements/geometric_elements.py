import math


class Vector:
    def __init__(self, x: float, y: float, z: float = 0):
        self.z = z
        self.y = y
        self.x = x

    @property
    def length(self) -> float:
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def __mul__(self, other: "Vector") -> "Vector":
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
