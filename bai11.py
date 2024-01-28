import fermat

if __name__ == "__main__":
        
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))

    if fermat.fermat_test(n)==True:
        print("N có thể là số nguyên tố")
    else:
        print("N không phải số nguyên tố")