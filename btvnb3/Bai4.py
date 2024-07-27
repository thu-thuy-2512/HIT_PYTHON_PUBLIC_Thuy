họ_tên = input("Họ tên: ")
a = list(họ_tên)
b = []
for i in range(len(a)):
    if not(a[i] == ' ' and (a[i - 1] == " " or i == 0)):
        b.append(a[i])
họ_tên = "".join(b)
họ_tên = họ_tên.title()
print("Định dạng chuẩn: ", họ_tên)