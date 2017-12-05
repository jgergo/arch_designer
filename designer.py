import input_reader as ir
from arch_elements import RoomBuilder
from arch_elements.room import arrange_rooms_on_x
from visualizer.matplot import MatPlot as MtPl
from shapely.geometry import Point
import pprint

if __name__ == '__main__':
    xls_path = r"C:\Users\jgerg\PycharmProjects\arch_designer"
    xls_name = r"\demo_input.xlsx"

    room_builder = RoomBuilder()

    data = ir.read_excel_by_line("".join([xls_path, xls_name]))
    pp = pprint.PrettyPrinter()

    rooms = [room_builder.create_room_from_xls(row[0], row[1], row[2]) for row in data]
    arrange_rooms_on_x(rooms)
    pltr = MtPl()
    pltr.plot_rooms(rooms)
    for room in rooms:
        print(room)
