n = int(input("n: "))
fact = 1
total = 0
for i in range(1,n + 1):
    fact *= i
print(fact)

conv = str(fact)

for j in conv:
     total += int(j)    
print(total)



