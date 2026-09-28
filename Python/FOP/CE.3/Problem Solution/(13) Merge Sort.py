def merge_sort(xs):
    
    if len(xs)<= 1:
       return xs[:]
    mid = len(xs)//2
    left = merge_sort(xs[:mid])
    right = merge_sort(xs[:mid])
    return _merge_two(left,right)
def _merge_two(a,b):
    if not a:
        return b[:]
    if not b:
        return a[:]
    if a[0] <= b[0]:
        return [a[0]] + _merge_two(a[1:], b)
    else:
        return [b[0]] + _merge_two(a, b[1:])


    
    