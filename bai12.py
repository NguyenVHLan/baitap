import millerrabin

if __name__ == "__main__":
        
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))

    if millerrabin.miller_rabin(n)==True:
        print("N có thể là số nguyên tố")
    else:
        print("N không phải số nguyên tố")