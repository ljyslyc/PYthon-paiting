import matplotlib.pyplot as plt
import numpy as np

size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
x = np.arange(size)

# just change n for the number of the types
total_width, n = 0.8, 3
width = total_width / n

# redraw the coordinates of x
x = x - (total_width - width) / 2

# here is the offset
plt.bar(x, a, width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()

plt.show()
