import numpy as np 
import matplotlib.pyplot as plt 
x = np.linspace(-5, 5, 100) 
y1 = x**2 
y2 = x**3 
fig, ax = plt.subplots() 

ax.plot(x,y1, label = 'y = x^2', color = 'blue') 
ax.plot(x,y2, label = 'y = x^3', color = 'red') 

plt.xlabel('x') 
plt.ylabel('y') 

plt.axhline(y = 0, color = 'black') 
plt.axvline(x = 0, color = 'black') 

plt.grid(True, linestyle = '--', alpha = 0.5) 
plt.legend()
plt.title('something') 
plt.show()