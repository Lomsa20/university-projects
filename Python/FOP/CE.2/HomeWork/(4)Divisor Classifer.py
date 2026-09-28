n = int(input("n: "))
div = []

for i in range(1, n +  1):
    if n % i == 0:
        div.append(i)
print("divisor", div)

# Classification
# Proper divisors are all divisors except the number itself

sum_proper = sum(div[:-1])

if len(div) == 2:
    print("Prime")
elif sum_proper == n:
    print("Perfect")
else:
    print("Neither")
    
    