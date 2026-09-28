def factorial(n):
    if n <= 1:
        return 1
    elif n <0:
        raise ValueError
    
    return n * factorial(n-1)
    
print(factorial(5))