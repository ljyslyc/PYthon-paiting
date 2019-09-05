import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.plot(x, x**4, label='biquadrate')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('simple line chart')
plt.legend()

plt.show()
