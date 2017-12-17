from .polygonal_element import PolygonalElement
from shapely.geometry import Polygon, Point
from .geometric_elements import Vector
from typing import List, Tuple
import math


class RvdRoom:
    def __init__(self, center_point: Vector, width: float, length: float):
        self.length = length
        self.width = width
        self.center_point = center_point
        self._xy_dims = Vector(width, length)
        self._normals = [Vector(-1, 0), Vector(0, 1), Vector(1, 0), Vector(0, -1)]

    @property
    def borders(self) -> List[Tuple[Vector, Vector]]:
        for v in self._normals:
            yield v, v * self._xy_dims

    def border_by_normal(self, normal: Vector) -> Tuple[Vector, Vector]:
        border = [b for b in self.borders if (b[0] + normal).length == 0][0]
        return border


class Room(PolygonalElement):
    def __init__(self, arch_id: int, polygon: Polygon, name: str, group: str):
        super().__init__(arch_id, polygon)
        self.group = group
        self.name = name

    @property
    def representative_name(self) -> str:
        return " ".join([str(self.arch_id), self.name, str(round(self.area, 2)), "m2", self.group])

    @property
    def mid_point(self) -> Point:
        return self.polygon.centroid

    @property
    def x(self) -> float:
        return self.mid_point.x

    @property
    def y(self) -> float:
        return self.mid_point.y

    @property
    def plot_name(self) -> str:
        return " ".join([str(self.arch_id), self.name, "\n", str(round(self.area, 2)), "m2", "\n", self.group])

    def __str__(self):
        return self.representative_name


class RoomCollector:
    def __init__(self):
        self._instances = []  # typing: List[Room]
        self.counter = 0

    def create_room(self, name: str, area: float, group: str, center_point: Point = Point(0, 0)):
        ratio = 1.5
        width_x = math.sqrt(area / ratio)
        length_y = ratio * width_x
        min_x = center_point.x
        min_y = center_point.y
        max_x = center_point.x + width_x
        max_y = center_point.y + length_y
        lin_ring = [(min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)]
        polygon = Polygon(lin_ring)
        self.counter += 1
        room = Room(self.counter, polygon, name, group)
        self._instances.append(room)

    def arrange_rooms_on_x(self):
        sum_l = 0
        for room in self._instances:
            room.move(Point(sum_l, 0))
            sum_l += room.width * 1.05

    def __iter__(self) -> Room:
        for i in self._instances:
            yield i
