def Selection_sort(a):
    arr = a[:]
    n = len(arr)
    for i in range(n- 1):
        min_idx = i
        if arr[j] < arr[min_idx]:
            min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"i={i}, min_idx={min_idx}, array={arr}")
    return arr
nums = list(map(int, input("Enter numbers: ").split()))
print("Sorted:", selection_sort_trace(nums))