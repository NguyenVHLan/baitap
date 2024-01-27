import math
import thuattoancoban

#A=[157, 0, 173, 23]
#B=[169, 1, 0, 64]
#W=8
#F=2147483647
#t=4
def phep_cong_mang(A,B,t,W):
    epsilon = 0
    list = [0] * t
    for i in range(t-1,-1,-1):
        x = 2 ** (W)
        result = (A[i]+B[i]+epsilon)%x
        list[i]=result
        if (A[i]+B[i]+epsilon)>=x:
            epsilon = 1
        else:
            epsilon = 0
    return epsilon, list

#print(phep_cong_mang(A,B,t,W))

#A=[0,11,173,248]
#B=[0,1,226,64]
def phep_tru_mang(A,B,t,W):
    epsilon = 0
    result_list = [0] * t
    for i in range(t-1,-1,-1):
        x = 2 ** (W)
        result = (A[i]-B[i]-epsilon)%x
        result_list[i]=result
        if (A[i]-B[i]-epsilon)<0:
            epsilon = 1
        else:
            epsilon = 0
    return epsilon, result_list

#print(phep_tru_mang(A,B,t,W))

def cong_tren_F(A,B,F,W):
    t = math.ceil(math.ceil(math.log2(F))/W)
    a = thuattoancoban.so_sang_mang(F,W,A)
    b = thuattoancoban.so_sang_mang(F,W,B)

    e,c = phep_cong_mang(a,b,t,W)
    if e == 1 :
        e,c = phep_tru_mang(c,2**(t*W),t,W)
    return c

def tru_tren_F(A,B,F,W):
    t = math.ceil(math.ceil(math.log2(F))/W)
    a = thuattoancoban.so_sang_mang(F,W,A)
    b = thuattoancoban.so_sang_mang(F,W,B)

    e,c = phep_tru_mang(a,b,t,W)
    if e == 1 :
        e,c = phep_cong_mang(c,2**(t*W),t,W)
    return c