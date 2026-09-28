x = float(input("x: "))
y = float(input("y: "))
r_in = float(input("r_inner: "))
r_out = float(input("r_outer: "))

d2 = x**2 + y**2
k = r_in**2<= d2 <= r_out
print(k)


