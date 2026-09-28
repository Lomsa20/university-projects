def Insertion_sort(arr):
    for i in range(1,len(arr)-1):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[i] > key:
            arr[j+ 1] = arr[j]
            j -= 1
        arr[j+ 1] = key
        