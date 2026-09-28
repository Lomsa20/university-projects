def Insertion_sort(arr):
    a= arr[:]
    n = len(arr)

    for i in range(1,n):
        key = a[i]
        j = i - 1

        while j >= 0 and (len(a[j]) > len(key)
                          or len(a[j]) == len(key) and a[j] > key):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
arr = ["bbb", "a", "cc", "aa", "c"]
print(Insertion_sort(arr))
