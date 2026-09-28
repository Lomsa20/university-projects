def power_set(xs):
    if not xs:
        return [[]]
   
    first = xs[0]
    rest = xs[1:]
   
    without_first = power_set(rest)
    with_first = [[first] + s for s in without_first]
    return without_first + with_first

print(power_set([1, 2, 3]))





























