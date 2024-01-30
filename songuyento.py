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
