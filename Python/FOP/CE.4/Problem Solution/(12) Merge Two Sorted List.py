def merge_two_sorted_lists(a, b):
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result


list1 = list(map(int, input("Enter first sorted list: ").split()))
list2 = list(map(int, input("Enter second sorted list: ").split()))

print(merge_two_sorted_lists(list1, list2))
