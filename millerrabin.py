import random

def miller_rabin(n,t):
    if t <= 0:
        t = 10
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    s=0
    x=n-1
    while x % 2 == 0:
        x = x // 2
        s = s + 1
    r=x

    for _ in range(t):
        a = random.randint(2,n-2)
        y = modulo_power(a,r,n)
        if (y != 1) and (y != n-1) :
            j=1
            while (j<=s-1) and (y!=n-1):
                y=modulo_power(y,2,n)
                if y==1:
                    return False
                j += 1
            if (y != n-1):
                return False
    
    return True

def modulo_power(a, b, m):
    if a % m == 0:
        return 0 
    result = 1
    a = a % m 
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    return result