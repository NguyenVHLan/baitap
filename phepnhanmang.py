import math
# phép nhân 2 mảng A,B
def phep_nhan_mang(A,B,t,W):
    # tạo mảng C[2t] để hứng kết quả
    C = [0]*(2*t)

    def dao_nguoc_mang(arr):
        return arr[::-1]
    
    # hàm chuyển UV sang U và V
    def chuyen_sang_U_V(number, W):
        binary_string = format(number, f'0{2*W}b') # đổi giá trị thành chuỗi string dài 2W với giá trị là các bit 01
        U = int(binary_string[:W], 2) # gán U và V là int có giá trị theo W bit sử dụng hệ cơ số 2
        V = int(binary_string[W:], 2)
        return U, V
    
    # đảo mảng
    a=dao_nguoc_mang(A)
    b=dao_nguoc_mang(B)

    # Bước 1
    for i in range(0,t,1):
        C[i]=0

    # Bước 2
    for i in range(0,t,1):
        # Bước 2.1
        U=0
        
        # Bước 2.2
        for j in range(0,t,1):
            UV = C[i+j] + a[i]*b[j] + U
            U,V = chuyen_sang_U_V(UV,W)
            C[i+j]=V

        # Bước 2.3
        C[i+t]=U

    # Bước 3
    return dao_nguoc_mang(C)

   


