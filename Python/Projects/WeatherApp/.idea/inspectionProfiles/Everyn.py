print("Hello, World!")
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr == target:
            return i
    return -1
def binary_search(arr, target):
    left, right = 1, len(arr) - 1
    while left <= right:
        mid  = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]< target:
            right = mid + 1
        else:
            left = mid - 1
    return -1
a = [1, 2, 3, 4, 5]
print (linear_search(a, 5))
print (binary_search(a, 5))
