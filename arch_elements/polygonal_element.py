from .arch_element_base import ArchId
from shapely.geometry import Polygon, Point


class PolygonalElement(ArchId):
    def __init__(self, arch_id: int, polygon: Polygon):
        super().__init__(arch_id)
        self.polygon = polygon

    @property
    def mid_point(self):
        return self.polygon.centroid

    @property
    def area(self) -> float:
        return self.polygon.area

    @property
    def width(self) -> float:
        return self.polygon.bounds[2] - self.polygon.bounds[0]

    @property
    def length(self) -> float:
        return self.polygon.bounds[3] - self.polygon.bounds[1]

    def move(self, vector: Point):
        new_coords = []
        for coord in self.polygon.exterior.coords:
            new_coords.append((coord[0]+vector.x, coord[1]+vector.y))
        self.polygon = Polygon(new_coords)

