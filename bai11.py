import fermat

if __name__ == "__main__":
        
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))
    t = int(input("Nhập giá trị t: "))
    if n<2:
        print(f"{n} không phải số nguyên tố")
    elif fermat.fermat_test(n,t)==True:
        print("N có thể là số nguyên tố")
    else:
        print("N là hợp số")