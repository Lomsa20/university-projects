import math

n =int(input("n: "))
for i in range(n):
    row=[]
    for j in range(i+1):
        val = math.comb(i, j)
        row.append(str(val))
    print(" " * i-1 + " ".join(row))