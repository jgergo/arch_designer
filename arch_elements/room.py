from .polygonal_element import PolygonalElement
from shapely.geometry import Polygon, Point
from typing import List
import math


class Room(PolygonalElement):
    def __init__(self, arch_id: int, polygon: Polygon, name: str, group: str):
        super().__init__(arch_id, polygon)
        self.group = group
        self.name = name

    @property
    def representative_name(self) -> str:
        return " ".join([str(self.arch_id), self.name, str(round(self.area, 2)), "m2", self.group])

    @property
    def plot_name(self) -> str:
        return " ".join([str(self.arch_id), self.name, "\n", str(round(self.area, 2)), "m2", "\n", self.group])

    def __str__(self):
        return self.representative_name


def arrange_rooms_on_x(rooms: List[Room]):
    sum_l = 0
    for room in rooms:
        room.move(Point(sum_l, 0))
        sum_l += room.width*1.05


class RoomBuilder:
    def __init__(self):
        self.counter = 0

    def create_room_from_xls(self, name: str, area: float, group: str) -> Room:
        ratio = 1.5
        x = math.sqrt(area / ratio)
        y = ratio*x
        lin_ring = [(0, 0), (0, y), (x, y), (x, 0)]
        polygon = Polygon(lin_ring)
        self.counter += 1
        room = Room(self.counter, polygon, name, group)
        return room
