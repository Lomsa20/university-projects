n = int(input("n:"))

def fib(n):
    a = 0
    b = 1
    for i in range(1, n+1):
        next = a+b
        a = b
        b = next 
        print("a=",a, "b=", b, "next= ", next)
    return next
res = fib(n)
print(res)
