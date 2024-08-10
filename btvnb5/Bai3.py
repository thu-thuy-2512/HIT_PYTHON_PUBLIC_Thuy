import random
N = int(input("Nhập số lượng tài khoản cần tạo: "))
tien_to_mat_khau = ["CNTT", "KHMT", "KTPM", "HTTT"]
tai_khoan = {}
for i in range(1, N+1):
    ma_sinh_vien = input(f"ma sinh vien thu {i}:")
    tien_to = random.choice(tien_to_mat_khau)
    mat_khau = tien_to + ma_sinh_vien
    tai_khoan[f"Account {i}"] = {
        "Username": ma_sinh_vien,
        "Password": mat_khau
    }
for key,value in tai_khoan.items():
    print(key,value)