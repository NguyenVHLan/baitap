import thuattoancoban, phepcongmang, phepnhanmang, math

def chuyen_sang_U_V(number, W):
        binary_string = format(number, f'0{2*W}b')
        U = int(binary_string[:W], 2)
        V = int(binary_string[W:], 2)
        return U, V

print(chuyen_sang_U_V(15872,8))