import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 1, 1, 1, 1, 1, 1]
z = [2, 4, 6, 8, 10, 12, 14]

x2 = [1, 2, 3, 4, 5, 6, 7]
y2 = [1, 1, 1, 1, 1, 1, 1]
z2 = [1, 3, 5, 7, 9, 11, 13]

ax.plot(x, y, z)
ax.plot(x2, y2, z2, color = 'red')

plt.show()