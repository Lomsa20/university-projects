def selection_sort(arr):
    a = arr[:]
    n = len(arr)
    for i in range(n-1): #points at num and assumes it's smallest
        min_idx = i
        for j in range(i+1,n):
            if (a[j][1], a[j][2] < a[min_idx][1], a[min_idx][2] < a[min_idx][2]):
                #Modification always happened there
                min_idx = j #we compare it with every num
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            #swaps it if it found smaller
students = [
    ("Alice", 90, 20),
    ("Bob", 95, 22),
    ("Charlie", 90, 18),
    ("David", 95, 19)
]

print(selection_sort(students))
