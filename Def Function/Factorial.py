n = int(input("n: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range (1, n+1):
            fact *= i
        return fact
result = factorial(n)
print(f"n factorial is {result}")