import random

def fermat_test(n, k=10):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    def fermat_check(a, n):
        if pow(a, n-1, n) != 1:
            return False
        return True
    
    for _ in range(k):
        a = random.randint(2, n-2)
        if not fermat_check(a, n):
            return "n là hợp số"
    return "n có thể là số nguyên tố"

# Sử dụng hàm để kiểm tra xem số n có phải là số nguyên tố hay không
print(fermat_test(383))  
