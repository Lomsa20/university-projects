print("a*x^2 + b*x + c = 0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
D = b**2 - 4*a*c

if D > 0 :
    root1 = (-b -D**0.5)/ 2*a
    root2 = (-b +D**0.5)/ 2*a
    print(f"their is two real answer: {root1}, {root2}")
if D == 0 :
    root3 = -b / 2*a
    print(f"their is one real answer: {root3}")
if D < 0 :
    print("their is no real answer")


