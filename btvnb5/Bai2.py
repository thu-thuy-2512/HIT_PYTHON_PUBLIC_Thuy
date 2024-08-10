string = input("Nhập một chuỗi: ")
dem = {}
for char in string:
    if char in dem:
        dem[char] += 1
    else:
        dem[char] = 1
print(dem)