# tìm ước chung lớn nhất của a và b
def gcd(a,b):
    while b!=0:
        a,b = b, a%b
    return a
