import thuattoancoban, phepcongmang, phepnhanmang, math

W=8
a=2147483646
b=4147483647 
F=2147483646

print(thuattoancoban.so_sang_mang(F,W,a))
print(thuattoancoban.so_sang_mang(F,W,b))
print(phepcongmang.phep_cong_mang(thuattoancoban.so_sang_mang(F,W,a),thuattoancoban.so_sang_mang(F,W,b),math.ceil(math.ceil(math.log2(F)/W)),W))
#print(phepcongmang.cong_tren_F(a,b,F,W))
#print(phepcongmang.phep_tru_mang(thuattoancoban.so_sang_mang(F,W,a),thuattoancoban.so_sang_mang(F,W,b),math.ceil(math.ceil(math.log2(F)/W)),W))
#print(phepcongmang.tru_tren_F(a,b,F,W))