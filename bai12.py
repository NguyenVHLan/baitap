import millerrabin

if __name__ == "__main__":
        
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))
  
    t = int(input("Nhập giá trị t: "))
 
    if n<2:
        print(f"{n} không phải số nguyên tố")
    elif millerrabin.miller_rabin(n,t)==True:
        print(f"{n} có thể là số nguyên tố")
    else:
        print(f"{n} là hợp số")