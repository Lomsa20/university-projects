def greater(arr):
    stack = []
    res = [-1]* len(arr)
    for i in range(len(arr)-1, -1, -1): #5,4,3,2,1
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(arr[i])
    return res
print(greater([1,2,4,5,7,6,3,5]))










