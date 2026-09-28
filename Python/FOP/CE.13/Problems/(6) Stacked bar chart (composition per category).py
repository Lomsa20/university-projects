import numpy as np
import matplotlib.pyplot as plt

product = ['A', 'B','C','D','E']
sales = np.array([123,124,186,200,440])
manufacture = np.array([12, 11,23,20,30])
profit = np.array([80,81,130,150,320])
width = 0.3

x = np.arange(len(product))
fig, ax = plt.subplots()
plt.bar(x,manufacture, label = 'manufacture',color='navy')
plt.bar(x,sales, bottom = manufacture, label='sales',color='gold')
plt.bar(x,profit,bottom = manufacture + sales,label='profit',color='green' )


plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(x,product)
plt.legend()
plt.show()