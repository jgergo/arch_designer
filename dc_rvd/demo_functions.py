from arch_elements import RoomCollector, Room, RvdRoom
from geometryc_elements import Vector
from typing import List


def rvd(rooms: List[RvdRoom]):
    """
    1. filter rooms into 45° quadratic directions: left, right, before, after -> 4 list of rooms
    TODO: filter rooms by room side ratio proportional see: 01_filtering method.jpg

    :param rooms:
    :return:
    """

    for room in rooms:
        left = [e for e in rooms if room.x - e.x > abs(room.y - e.y)]
        right = [e for e in rooms if e.x - room.x > abs(room.y - e.y)]
        top = [e for e in rooms if abs(room.x - e.x) < e.y - room.y]
        bottom = [e for e in rooms if abs(room.x - e.x) < room.y - e.y]

        for border in room.borders:
            border_normal = border[0] # type: Vector
            # elements = [e for e in rooms if ]
            for element in left:
                element_border = element.border_by_normal(border_normal)







