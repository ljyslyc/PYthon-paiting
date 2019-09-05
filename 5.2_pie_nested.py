import matplotlib.pyplot as plt
import numpy as np

# set the width of each ring
size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

# get the color randomly by get_cmap
cmap = plt.get_cmap("tab20c")
outer_colors = cmap(np.arange(3) * 4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

print(vals.sum(axis=1))
# [92. 77. 39.]

plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
        wedgeprops=dict(width=size, edgecolor='w'))
print(vals.flatten())
# [60. 32. 37. 40. 29. 10.]

plt.pie(vals.flatten(), radius=1 - size, colors=inner_colors,
        wedgeprops=dict(width=size, edgecolor='w'))

# equal makes it a perfect circle
plt.axis('equal')
plt.show()
