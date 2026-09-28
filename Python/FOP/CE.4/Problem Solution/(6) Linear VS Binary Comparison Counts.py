def Linear_search(arr, t):
    comps = 0
    for i in range(len(arr)):
        comps += 1
        if i == t:
            return comps
    return comps # Target absent -> n comparisons

def Binary_search(arr, t):
    low, high = 0, len(arr)-1
    comps = 0
    while low <= high:
        mid = (low + high) // 2
        comps += 1
        if arr[mid] < t:
            low = mid + 1
        elif arr[mid] > t:
            high = mid -1
        else:
            return comps
    return comps # Target absent → log₂(n)+1 comparisons
# Experiment
n = int(input("Enter n: "))
arr = list(range(0, 2 * n, 2)) # Sorted even numbers
t = 2 * n + 1 # Odd number, guaranteed absent
print(n, Linear_search(arr, t), Binary_search(arr, t))