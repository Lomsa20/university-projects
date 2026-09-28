def count_occurrences (xs, item):
    if not xs:
        return 0
    else:
        return(1 if xs[0] == item else 0)+count_occurrences(xs[1:], item)
print(count_occurrences([8,8,8,8, 12,"a", "a"], 8))









