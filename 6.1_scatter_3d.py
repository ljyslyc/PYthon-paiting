import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # projection '3d' # noqa

data = np.random.randint(0, 255, size=[40, 40, 40])

x, y, z = data[0], data[1], data[2]
ax = plt.subplot(111, projection='3d')  # create a 3D drawing project
#  divide the data points into three parts with a distinction in color
ax.scatter(x[:10], y[:10], z[:10], c='y')  # draw data points
ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

ax.set_zlabel('Z')  # axes
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
