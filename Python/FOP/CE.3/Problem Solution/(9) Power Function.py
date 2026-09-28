def pow_fast(x,n):
    if n <0:
        return ValueError
    elif  n== 0 :
        return 1
    elif n % 2 == 0:
        return x* pow_fast( x*x, n/2)
    else:
        return x*pow_fast(x, n - 1)
print(pow_fast(12, 1231))
 










