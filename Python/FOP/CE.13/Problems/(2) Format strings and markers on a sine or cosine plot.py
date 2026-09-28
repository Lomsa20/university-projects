import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*(np.pi), 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()
plt.plot(x,y1, 'bo')
plt.plot(x,y2, 'r--')

plt.xlabel('x')
plt.ylabel('y')

plt.legend(['sin(x)', 'cos(x)'])
plt.title('sin(x), cos(x)')

plt.show()