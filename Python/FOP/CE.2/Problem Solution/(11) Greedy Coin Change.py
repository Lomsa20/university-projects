amount = int(input("Amount(cents): "))
den = [100, 50, 20, 10, 5, 2, 1]
counts = [0]*len(den)
rem = amount

for i, d in enumerate(den):
    if rem == 0:
        break
    cnt = rem // d
    counts[i] = cnt
    rem = rem % d
print(sum(counts))
print(" " .join(str(x) for x in counts))