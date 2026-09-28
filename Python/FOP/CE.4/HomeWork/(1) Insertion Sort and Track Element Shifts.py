def insertion_sort(arr):
    a = arr[:]
    log = []

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            log.append(f'move {a[j]} from index {j} to index {j+1}')
            a[j + 1] = a[j]
            j -= 1

        if j + 1 != i:
            log.append(f'insert {key} at index {j+1}')
            a[j + 1] = key

    return a, log

arr = [1,4,2,3]
print(insertion_sort(arr))