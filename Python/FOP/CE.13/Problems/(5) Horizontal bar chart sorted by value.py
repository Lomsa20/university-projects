import numpy as np
import matplotlib.pyplot as plt

val = np.array([2,1,4,3,6,5,7,8])
name = np.array(['A','B','C','D','E','F','G','H'])

idx = np.argsort(val)[::-1]
val_sorted = val[idx]
name_sorted = name[idx]

plt.barh(name_sorted, val_sorted)

for i,v in enumerate(val_sorted):
    # i = the row number (y-axis position),
    # v = the length of the bar (x-axis value)
    plt.text(v + 0.1, i, str(v), va = 'center')
    #v + 0.1 → x-position of the text slightly past the end of the bar
    # i → y-position of the text (the row number on the y-axis)
    # str(v) → text to display (the value itself)
    # va='center' → vertically aligns text with the middle of the bar
plt.xlabel('Value')
plt.title('Value distribution')
plt.show()