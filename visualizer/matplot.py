from matplotlib import pyplot as plt
from arch_elements import Room
from typing import List


class MatPlot:
    def __init__(self):
        self.fig = plt.figure(1, figsize=(20, 10), dpi=90)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_aspect(1)

    def plot_rooms(self, rooms: List[Room]):
        for room in rooms:
            x, y = room.polygon.exterior.xy
            self.ax.plot(x, y)
            self.ax.text(room.mid_point.x, room.mid_point.y, room.plot_name, horizontalalignment='center',
                         verticalalignment='center')

        plt.show()
