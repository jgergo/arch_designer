import numpy as np
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
from voronoi.vor_methods import voronoi_finite_polygons_2d

N = 15

x = [np.random.randint(0, 10) for _ in range(N)]
y = [np.random.randint(0, 10) for _ in range(N)]

points = np.array(list(zip(x, y)))

vor = Voronoi(points)

regions, vertices = voronoi_finite_polygons_2d(vor)

for region in regions:
    polygon = vertices[region]
    plt.fill(*zip(*polygon), alpha=0.4)

plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(vor.vertices[:, 0], vor.vertices[:, 1], '*')

for simplex in vor.ridge_vertices:
     simplex = np.asarray(simplex)
     if np.all(simplex >= 0):
         plt.plot(vor.vertices[simplex, 0], vor.vertices[simplex, 1], 'k-')

plt.show()

for i, reg in enumerate(vor.regions):
    print (reg)


