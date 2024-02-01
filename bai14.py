import millerrabin

if __name__ == "__main__":
      
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))
    
    m = int(input("Nhập giá trị m: "))
    
    t = int(input("Nhập giá trị t: "))
    

    A=[]
    if m<n:
        m, n = n, m

    for i in range(n,m+1):
        if millerrabin.miller_rabin(i,t)==True:
            A.append(i)
    print("Các số nguyên tố có trong khoảng là:", A)