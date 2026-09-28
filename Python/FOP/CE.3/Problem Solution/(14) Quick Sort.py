def quick_sort(xs):
    if len(xs)<= 1:
        return xs[:]
    pivot = xs[0]
    less_eq = [x for x in xs[1:] if x <= pivot]
    greater = [x for x in xs[1:] if x > pivot]
    return quick_sort(less_eq) + [pivot] + quick_sort(greater)
print(quick_sort([1,23,432,12,3,4,56,7,89,3,21,]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    