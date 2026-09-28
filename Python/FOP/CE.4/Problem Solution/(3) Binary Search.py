def binary_search(arr,target):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
nums = input('Enter sorted nums: ')
arr = nums.split()
arr = [int(x) for x in arr]

t = int(input('target: '))
print(binary_search(arr, t))