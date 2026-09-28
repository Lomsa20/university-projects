def selection_sort(arr):
    a = arr[:]
    log = []
    n = len(a)

    for i in range(n - 1):
        min_idx = i
        log.append(f"start pass {i}, assume min = {a[min_idx]} at index {min_idx}")

        for j in range(i + 1, n):
            log.append(f"compare {a[j]} (index {j}) with {a[min_idx]} (index {min_idx})")
            if a[j] < a[min_idx]:
                min_idx = j
                log.append(f"new min found: {a[min_idx]} at index {min_idx}")

        if min_idx != i:
            log.append(f"swap {a[i]} (index {i}) with {a[min_idx]} (index {min_idx})")
            a[i], a[min_idx] = a[min_idx], a[i]

    return a, log
