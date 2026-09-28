a = int(input("a: "))
b = int(input("b: "))

for n in range (a, b + 1):
    if  n < 2:
        continue
    is_prime = True
    for i in range(2, n):
        if n % i  == 0:  #we write this because we are interested of prime number so this will divedi n 
            is_prime = False
            break
    if is_prime:
        print(n)
        
