import numpy as np
import matplotlib.pyplot as plt

# Data
products = ['A','B','C','D','E',]
sales = [120,150,90, 70, 190]
profit = [20, 40,30, 60,90]

# Positions
x = np.arange(len(products))
width = 0.35

# Plot
plt.bar(x - width/2, sales, width, label='Sales')
plt.bar(x + width/2, profit, width, label='Profit')

# Labels & title
plt.xlabel('Products')
plt.ylabel('Amount')
plt.title('Sales vs Profit by Product')
plt.xticks(x, products)
plt.legend()

plt.show()
