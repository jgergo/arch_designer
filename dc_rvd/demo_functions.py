from arch_elements import RoomCollector


def rvd(rooms: RoomCollector):
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
            elements = [e for e in rooms if ]





