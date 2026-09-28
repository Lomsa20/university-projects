def get_intersection(k = float, i = float):
    a, b = k, i
    while a != b:
        a = a.next if a else i
        b = b.next if a else k
    return a