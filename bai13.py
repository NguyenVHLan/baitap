import fermat

if __name__ == "__main__":
      
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))
    m = int(input("Nhập giá trị m: "))
    A=[]
    if m<n:
        m, n = n, m

    for i in range(n,m+1):
        if fermat.fermat_test(i)==True:
            A.append(i)
    print("Các số nguyên tố có trong khoảng là:", A)


