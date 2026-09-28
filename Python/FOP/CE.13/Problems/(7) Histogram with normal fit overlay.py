import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, exp

# Sample data
data = np.random.normal(50, 10, 1000)

# Sample mean and std
mu = np.mean(data)
sigma = np.std(data, ddof=1)   # sample std, not population

# Histogram (normalized)
plt.hist(data, bins=30, density=True, alpha=0.6, label='Histogram')

# Normal PDF
x = np.linspace(min(data), max(data), 300)
pdf = (1 / (sigma * sqrt(2 * pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

plt.plot(x, pdf, linewidth=2, label='Normal PDF')

plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram with Normal PDF Overlay')
plt.legend()
plt.show()
