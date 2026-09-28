def bubble_sort(a):
    arr = a[:]
    n = len(arr)
    end = n - 1
    passes = 0
    swaps = 0

    while end > 0:
        new_end = -1
        for j in range(end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                new_end = j
        passes += 1
        if new_end == -1:
            break
        end = new_end

    return arr, passes, swaps
text = input("Enter numbers: ")
parts = text.split()
nums = [int(x) for x in parts]
print(bubble_sort(nums))