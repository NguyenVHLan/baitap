import random

def miller_rabin(n,t):
    s=0
    x=n-1
    while x % 2 == 0:
        x = x // 2
        s = s + 1
    r=x

    for _ in range(t):
        a = random.randint(2,n-2)
        y = pow(a,r,n)
        if (y != 1) and (y != n-1) :
            j=1
            while (j<=s-1) and (y!=n-1):
                y=pow(y,y,n)
                print(y)
                if y==1:
                    return("hợp số")
                j += 1
            if (y != n-1):
                return("hợp số")
    
    return("nguyên tố")

print(miller_rabin(383,10))