
def pi_series_iter(n):
    res = 0
    for i in range(1, n + 1):
        res += 1 / (i ** 2)
    return res

def pi_approx_iter(n):
    x = pi_series_iter(n)
    return (6 * x) ** 0.5

# main part
n = int(input("Enter the number of terms (n): "))
approx_pi = pi_approx_iter(n)

print(f"Approximation of π using {n} terms is: {approx_pi}")




