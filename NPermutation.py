import math

def getNPermutation(n,k):
    if n == 1:
        return 1
    if n == 2:
        return math.comb(k*n,k)/2
    if n >= 3:
        return math.comb(k*n,k)