import input_reader as ir
from arch_elements import RoomCollector
from visualizer.matplot import MatPlot as MtPl
from shapely.geometry import Point
import pprint

if __name__ == '__main__':
    xls_path = r"C:\Users\jgerg\PycharmProjects\arch_designer"
    xls_name = r"\demo_input.xlsx"

    demo_inputs = [("Room 1", 20.0, "g", Point(5, 5)),
                   ("Room 2", 30.0, "g", Point(10, 4)),
                   ("Room 3", 7.0, "g", Point(6, 10)),
                   ("Room 4", 12.0, "g", Point(8, 9)),
                   ("Room 5", 2.0, "g", Point(9, 7))]

    room_collector = RoomCollector()

    data = ir.read_excel_by_line("".join([xls_path, xls_name]))
    pp = pprint.PrettyPrinter()

    # xls
    # rooms = [room_collector.create_room(row[0], row[1], row[2]) for row in data]

    # inline
    rooms = [room_collector.create_room(demo_input[0], demo_input[1], demo_input[2], demo_input[3]) for demo_input in
             demo_inputs]
    # room_collector.arrange_rooms_on_x()
    pltr = MtPl()
    pltr.plot_rooms(room_collector.instances)
    for room in rooms:
        print(room)
