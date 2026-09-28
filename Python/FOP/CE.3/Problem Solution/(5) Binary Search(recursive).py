def binary_search(sorted_list, target, left, right):
    #or we can use extra def and make it more readable
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if sorted_list[mid] == target:
        return mid
    elif sorted_list[mid] < target:
        return binary_search(sorted_list, target, mid + 1, right)
    else:
        return binary_search(sorted_list, target, left, mid - 1)


lst = [1, 2, 3, 4, 5, 23, 12, 32, 45]
lst.sort()
target = 3
print(binary_search(lst, target, 0, len(lst) - 1))
