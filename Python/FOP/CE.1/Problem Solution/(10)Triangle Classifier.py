a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a + b < c) or (b + c < a) or (a + c < b):
    print("invalid")
elif a == b == c:
    print("Equilateral")
elif (a == b) or (b == c) or (a == c):
    print("Isosceles")
else:
    print("Scalene")


