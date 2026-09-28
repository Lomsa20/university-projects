import numpy as np
import matplotlib.pyplot as plt


sample1 = np.random.normal(50, 10, 1000)
sample2 = np.random.normal(70,10, 1000)

plt.hist(sample1, bins = 100, density = True, alpha = 0.75, label = "Sample1")
plt.hist(sample2, bins = 100, density = True, alpha = 0.75, label = "Sample2")
plt.legend()
plt.ylabel("Probability")
plt.xlabel("Sample")
plt.grid(True,  ls = '--')
plt.title("Histogram of Samples")
plt.show()