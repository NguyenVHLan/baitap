import math,random

def eratosthenes(n):
    if n<0: 
        return []
    primes = [True] * (n+1)
    primes[0] = primes[1] = False  # 0 và 1 không phải là số nguyên tố

    p = 2
    while p**2 <= n:
        if primes[p] == True:
            for i in range(p**2, n+1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n+1) if primes[i]]

def era_phan_doan(n,m):
    if n>m:
        n,m=m,n
    if n<2:
        n=2

    primes = [True] * (m-n+1)

    i=2
    while i**2 <= m:
        if primes[i]:
            for j in range(max(i * i, ((n + i - 1) // i) * i), m + 1, i):
                primes[j-n] = False
        i+=1
    
    return [i for i in range(n, m + 1) if primes[i - n]]



