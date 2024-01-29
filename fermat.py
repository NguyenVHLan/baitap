import random
# Sử dụng hàm để kiểm tra xem số n có phải là số nguyên tố hay không
def fermat_test(n, k=10):
    if k <= 0:
        k = 10
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
        a = random.randint(2, n-1)
        if not fermat_check(a, n):
            return False
    return True

def modulo_power(a, b, m):
    result = 1
    a = a % m 
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    return result
