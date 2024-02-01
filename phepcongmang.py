import math
import thuattoancoban

# phép cộng hai mảng a và b
def phep_cong_mang(A,B,t,W):
    # tạo bit nhớ và mảng
    epsilon = 0
    list = [0] * t

    # chạy mảng từ t-1 tới 0 (mảng lưu ngược lại A0 -> A3)
    for i in range(t-1,-1,-1):
        x = 2 ** (W)
        list[i]=(A[i]+B[i]+epsilon)
        if list[i]>=x:
            epsilon = 1
            list[i]=list[i]%x
        else:
            epsilon = 0
    return epsilon, list

# phép trừ hai mảng a và b
def phep_tru_mang(A,B,t,W):
    # tạo bit nhớ và mảng
    epsilon = 0
    list = [0] * t

    # chạy mảng từ t-1 tới 0 (mảng lưu ngược lại A0 -> A3)
    for i in range(t-1,-1,-1):
        x = 2 ** (W)
        list[i] = A[i]-B[i]-epsilon
        if list[i]<0:
            epsilon = 1
            list[i]=list[i]%x
        else:
            epsilon = 0
    return epsilon, list

# phép cộng hai mảng a và b trên Fp
def cong_tren_F(A,B,F,W):
    # tính t là số lượng từ
    t = math.ceil(math.ceil(math.log2(F))/W)

    # đổi các giá trị sang mảng
    a = thuattoancoban.so_sang_mang(F,W,A)
    b = thuattoancoban.so_sang_mang(F,W,B)
    p = thuattoancoban.so_sang_mang(F,W,F)

    e,c = phep_cong_mang(a,b,t,W)
    if e==1:
        e,c = phep_tru_mang(c,p,t,W)
    elif e==0:
        e,c = phep_tru_mang(c,p,t,W)
    return c

# phép cộng hai mảng a và b trên Fp
def tru_tren_F(A,B,F,W):
    # tính t là số lượng từ
    t = math.ceil(math.ceil(math.log2(F))/W)

    # đổi các giá trị sang mảng
    a = thuattoancoban.so_sang_mang(F,W,A)
    b = thuattoancoban.so_sang_mang(F,W,B)

    e,c = phep_tru_mang(a,b,t,W)
    if e == 1 :
        p=thuattoancoban.so_sang_mang(F,W,F)
        e,c = phep_cong_mang(c,p,t,W)
    return c