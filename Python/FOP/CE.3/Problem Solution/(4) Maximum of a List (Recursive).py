def max_list(xs):
    if not xs:
        raise ValueError
    if len(xs) == 1:
        return xs[0]
    tail_max = max_list(xs[1:])
    return xs[0] if xs[0] > tail_max else tail_max
print(max_list([1,4,9,32,3,5,12,21,43,45,436,321,3,2,43,6,43,5432,3,12,43,252,2,314,2,3,2,312,4,32,5,43,56,34,6,3,645,]))






