def permutation(xs):
    if not xs:
        return [[]]  # base case: one permutation of empty list
    out = []
    for i in range(len(xs)):
        first = xs[i]
        rest = xs[:i] + xs[i + 1:]
        for p in permutation(rest):
            out.append([first] + p)
    return out

# Example with a list
print(permutation([1, 2]))  

# Example with an integer by converting to digits
num = 12
digits = [int(d) for d in str(num)]
print(permutation(digits))
