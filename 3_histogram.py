import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2018)

mu1, sigma1 = 100, 15
mu2, sigma2 = 80, 20
x1 = mu1 + sigma1 * np.random.randn(10000)
x2 = mu2 + sigma2 * np.random.randn(10000)

# the histogram of the data
# 50：divide the data into 50 groups
# facecolor: color; alpha: transparency
# density：it's density rather than specific value

# n: probability values; bins: specific values; patches: histogram objects
n1, bins1, patches1 = plt.hist(x1, 50, density=True, facecolor='g', alpha=1)
n2, bins2, patches2 = plt.hist(x2, 50, density=True, facecolor='r', alpha=0.5)

plt.xlabel('smarts')
plt.ylabel('probability')
plt.title('histogram of iq')

plt.text(110, 0.025, r'$\mu=100, \ \sigma=15$')
plt.text(50, 0.025, r'$\mu=80, \ \sigma=15$')

plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show()
