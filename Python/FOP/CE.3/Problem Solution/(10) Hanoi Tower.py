def hanoi(n, src, aux, dst): #src = start, aux = helper, dst = finish
    if n == 0 :
        return []
    moves1 = hanoi(n-1, src,dst,aux) #move the top  n-1 disks to aux a.k.a. helper peg

    move= [ (src, dst)] # this move the biggest disk from src to dst
    moves2= hanoi(n-1,aux,src,dst) #move the n-1 disks from helper peg to destination
    return moves1 + move + moves2
print(hanoi(5, "a", "b", "c"))