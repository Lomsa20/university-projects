a = int(input("a: "))
b = int(input("b: "))
def bigger(a,b):
    if a > b:
        return a
    else:
        return b
big = bigger(a,b)
print(f"bigger is {big}")