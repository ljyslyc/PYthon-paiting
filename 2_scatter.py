import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 5.0, 0.2)

# red dashes and black solids
plt.plot(x, x, 'r--', x, x**1.5, 'k-')
# blue squares and green triangles
plt.plot(x, x**2, 'bs', x, x**3, 'g^')
plt.show()
