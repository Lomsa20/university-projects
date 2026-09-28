def sum_list(xs):
    if not xs :
        return 0
    else:
        return xs[0] + sum_list(xs[1:]) 
#Because of xs[0] is first element we write like this 
#and sum_list(xs[1:]) this mean that every element that 
#is in list except first one because we write it already                

print(sum_list([1,2,3,4]))





