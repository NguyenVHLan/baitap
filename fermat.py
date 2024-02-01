import random,math

# hàm kiểm tra xem số n có phải là số nguyên tố hay không
def fermat_test(n, k):
    # loại các điều kiện n
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # dùng định lý fermat kiểm tra n có phải số nguyên tố với cơ sở là a hay ko :: a^(n-1) mod n đồng dư 1 => n là nguyên tố
    def fermat_check(a, n):
        if modulo_power(a, n-1, n) != 1:
            return False
        return True
    
    # kiểm tra n với k lần thử
    for _ in range(k):
        a = random.randint(2,n-1)
        if not fermat_check(a, n):
            return False
    return True

# hàm tính a^b mod m
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


