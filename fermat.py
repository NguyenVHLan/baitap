import random,math
# Sử dụng hàm để kiểm tra xem số n có phải là số nguyên tố hay không
def fermat_test(n, k):
    if k <= math.sqrt(n):
        k=math.ceil(math.sqrt(n))
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    def fermat_check(a, n):
        if modulo_power(a, n-1, n) != 1:
            return False
        return True
    
    for _ in range(k):
        a = random.randint(2,n-1)
        if not fermat_check(a, n):
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


