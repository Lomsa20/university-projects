import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)  

b[0] = 99         
b[2][0] = 77      

print(a)  
print(b)  