from matplotlib import pyplot as plt
from shapely.geometry import Polygon
from arch_elements import RoomCollector
from typing import List


class MatPlot:
    def __init__(self):
        self.fig = plt.figure(1, figsize=(20, 10), dpi=90)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_aspect(1)

    def plot_rooms(self, rooms: RoomCollector):
        for room in rooms:
            self.plot_polygon(room.polygon)
            self.ax.plot(room.mid_point.x, room.mid_point.y)
            self.ax.text(room.mid_point.x, room.mid_point.y, room.plot_name, horizontalalignment='center',
                         verticalalignment='center')

        plt.draw()
        plt.pause(0.1)
        plt.waitforbuttonpress()

    def plot_polygon(self, polygon: Polygon):
        x, y = polygon.exterior.xy
        self.ax.plot(x, y)
