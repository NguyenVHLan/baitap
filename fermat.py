import random
# Sử dụng hàm để kiểm tra xem số n có phải là số nguyên tố hay không
def fermat_test(n, k=10):
    if n <= 1:
        return "n không phải số nguyên tố"
    if n == 2 or n == 3:
        return "n là số nguyên tố"
    if n % 2 == 0:
        return "n là số chẵn"
    
    def fermat_check(a, n):
        if pow(a, n-1, n) != 1:
            return False
        return True
    
    for _ in range(k):
        a = random.randint(2, n-1)
        if not fermat_check(a, n):
            return "n là hợp số"
    return "n có thể là số nguyên tố"

print(fermat_test(383))  
