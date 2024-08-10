cau_hinh = {
    "n": 1500,
    "m": 2,
    "CLUSTERS": 3,
    "ITER": 10000,
    "METHOD": "FCM",
    "MEASURE": "EUCLIDEAN",
    "YEARS": 51
}
print("Nội dung từ điển cấu hình ban đầu:")
print(cau_hinh)
cau_hinh["MEASURE"] = "MANHATAN"
print("\nSau khi sửa thông số MEASURE:")
print(cau_hinh)
method = cau_hinh.get("METHOD")
print(f"\nThông số METHOD hiện đang được đặt là: {method}")
cau_hinh["LOSS FUNCTION"] = "NORM_2"
print("\nSau khi bổ sung thêm thông số 'LOSS FUNCTION':")
print(cau_hinh)
cau_hinh.pop("YEARS", None)
print("\nSau khi xóa thông số YEARS:")
print(cau_hinh)
S = input("\nNhập một chuỗi S: ")
if S in cau_hinh.values():
    print(f"Chuỗi S trùng với một giá trị trong từ điển: {S}")
else:
    print("Chuỗi S không trùng với giá trị nào trong từ điển.")
tap_gia_tri = set(cau_hinh.values())
print("\nSet chứa toàn bộ giá trị của các thông số:")
print(tap_gia_tri)
danh_sach_gia_tri = list(cau_hinh.values())
print("\nList chứa toàn bộ giá trị của các thông số:")
print(danh_sach_gia_tri)
