import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*(np.pi), 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

y3 = np.where(np.abs(y3) > 10, np.nan, y3)
fig, axs = plt.subplots(1, 3,sharex = True, figsize = (10,5))

# First Column
axs[0].plot(x,y1, 'o', color = 'navy',label = 'sin(x)')
axs[0].set_title('sin(x)')
axs[0].grid(True, linestyle = '-', alpha = 0.2)
axs[0].legend()

# Second Column
axs[1].plot(x,y2, 'o', color = 'blue', label = 'cos(x)')
axs[1].set_title('cos(x)')
axs[1].grid(True, linestyle = '-', alpha = 0.2)
axs[1].legend()

# Third Column
axs[2].plot(x,y3, 'o', color = 'aqua', label = 'tan(x)')
axs[2].set_title('tan(x)')
axs[2].grid(True, linestyle = '-', alpha = 0.2)
axs[2].legend()

# Common labels
for ax in axs:
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axhline(y = 0, color = 'black')
    ax.axvline(x = 0, color = 'black')
plt.tight_layout()
plt.show()
