import numpy as np
from scipy.spatial import Voronoi
import matplotlib.pyplot as plt

points = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1.5], [1, 3], [2, 0], [2, 1.5], [2, 2]])

vor = Voronoi(points)

print(vor.vertices)

plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(vor.vertices[:, 0], vor.vertices[:, 1], '*')
plt.xlim(-1, 4); plt.ylim(-1, 4)

for simplex in vor.ridge_vertices:
     simplex = np.asarray(simplex)
     if np.all(simplex >= 0):
         plt.plot(vor.vertices[simplex, 0], vor.vertices[simplex, 1], 'k-')

center = points.mean(axis=0)
for pointidx, simplex in zip(vor.ridge_points, vor.ridge_vertices):
    simplex = np.asarray(simplex)
    if np.any(simplex < 0):
        i = simplex[simplex >= 0][0] # finite end Voronoi vertex
        t = points[pointidx[1]] - points[pointidx[0]]  # tangent
        t = t / np.linalg.norm(t)
        n = np.array([-t[1], t[0]]) # normal
        midpoint = points[pointidx].mean(axis=0)
        far_point = vor.vertices[i] + np.sign(np.dot(midpoint - center, n)) * n * 100
        plt.plot([vor.vertices[i,0], far_point[0]],
                 [vor.vertices[i,1], far_point[1]], 'k--')
plt.show()