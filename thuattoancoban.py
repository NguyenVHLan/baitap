import math

# Thuật toán chuyển từ số sang mảng:
def so_sang_mang(F, W, a):
    list = []
    m = math.ceil(math.log2(F))
    t = math.ceil(m / W)

    for i in range(1, t + 1):
        x = 2 ** ((t - i) * W)
        b = a // x
        a = a % x
        list.append(b)

    return list

# Thuật toán chuyển từ mảng sang số:
def mang_sang_so(F, W, A):
    m = math.ceil(math.log2(F))
    t = math.ceil(m / W)

    result = 0
    for i in range(0, t ):
        x = 2 ** ((t - 1 - i) * W)
        result += A[i]* x

    return result
