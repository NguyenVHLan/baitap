import songuyento

if __name__ == "__main__":
        
    # Nhập giá trị 
    n = int(input("Nhập giá trị n: "))

    # Tìm các số nguyên tố 
    print("Các số nguyên tố nhỏ hơn hoặc bằng", n, "là:", songuyento.eratosthenes(n))