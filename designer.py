import input_reader as ir
from dc_rvd.demo_functions import rvd
from arch_elements import RoomCollector, RvdRoom
from geometryc_elements import Vector
from visualizer.matplot import MatPlot as MtPl
import numpy as np
from scipy.spatial import voronoi_plot_2d, KDTree
import scipy.spatial as sp



from shapely.geometry import Point
import pprint

if __name__ == '__main__':
    xls_path = r"C:\Users\jgerg\PycharmProjects\arch_designer"
    xls_name = r"\demo_input.xlsx"

    # demo_inputs = [("Room 1", 20.0, "g", Point(5, 5)),
    #                ("Room 2", 30.0, "g", Point(10, 4)),
    #                ("Room 3", 7.0, "g", Point(6, 10)),
    #                ("Room 4", 12.0, "g", Point(8, 9)),
    #                ("Room 5", 2.0, "g", Point(9, 7))]
    # room_collector = RoomCollector()

    demo_inputs_rvd = [(Vector(5, 5), 20.0, "Room 1"),
                       (Vector(10, 4), 30,0, "Room 2"),
                       (Vector(6, 10), 7.0, "Room 3"),
                       (Vector(8, 9), 12.0, "Room 4"),
                       (Vector(9, 7), 2.0, "Room 5")]

    # data = ir.read_excel_by_line("".join([xls_path, xls_name]))
    pp = pprint.PrettyPrinter()

    # xls
    # rooms = [room_collector.create_room(row[0], row[1], row[2]) for row in data]

    # inline
    rooms = [RvdRoom.from_area(demo_input[0], demo_input[1], demo_input[2]) for demo_input in
             demo_inputs_rvd]
    # room_collector.arrange_rooms_on_x()
    pltr = MtPl()
    pltr.plot_rooms(rooms)

    rvd(rooms)


