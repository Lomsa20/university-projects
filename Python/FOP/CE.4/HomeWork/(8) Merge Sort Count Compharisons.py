def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_counter = merge_sort(arr[:mid])
    right, right_counter = merge_sort(arr[mid:])
    merged, merge_counter = merge(left,right)
    total_count = left_counter + right_counter + merge_counter
    return merged, total_count
def merge(left, right):
    res = []
    i = j = 0
    counter = 0
    while i < len(left) and j < len(right):
        counter += 1
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res, counter
arr = [3, 1, 4, 2]
sorted_arr, comparisons = merge_sort(arr)
print(sorted_arr)      # [1, 2, 3, 4]
print(comparisons)     # 5 (total comparisons)
