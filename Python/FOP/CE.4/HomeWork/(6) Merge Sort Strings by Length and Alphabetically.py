def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)// 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]) or len(left[i]) == len(right[j]) and left[i] < right[j]:
            #main modification happened here
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
arr = ["cat", "a", "bat", "apple", "an"]
print(merge_sort(arr))
