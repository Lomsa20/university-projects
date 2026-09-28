arr = [int(x) for x in input("n: ").split(" ")]
k = int(input("k: "))
n = len(arr)
if k <= 0 or k > n:
    print("k is invalid")
else:
    cur_sum = 0
    
    for i in range(k):
         cur_sum += arr[i]  
    start = 0
    end = k
    best = cur_sum
    while end < n:
        cur_sum -= arr[start]
        cur_sum += arr[end]
        if cur_sum > best:
            best = cur_sum 
        start += 1
        end += 1
        
    print(best / k)

