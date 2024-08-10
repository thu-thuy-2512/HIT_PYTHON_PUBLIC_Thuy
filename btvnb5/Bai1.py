dict = { 
    2023603902:3.3,
    2023654890:2.0,
    2023643567:3.5,
    2023685437:1.9
}
dem = 0
for i in dict:
    if dict[i] >= 3.0 and dict[i] <= 3.5:
        dem += 1
print("so sinh vien co diem tongg ket trong doan [3.0,3.5] la:",dem)
dict[2023567489] = 3.2
xoa = []
for ma_sv,diem in dict.items():
    if diem < 2.0:
        xoa.append(ma_sv)
for ma_sv in xoa:
    dict.pop(ma_sv)
for ma_sv,diem in dict.items():
    print(ma_sv,diem)