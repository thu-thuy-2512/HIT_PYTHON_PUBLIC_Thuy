x = int(input("x = "))
while x < 1 or x > 1000:
    x = int(input("x = "))
print("Nhập số nguyên x = ", x)
a = x // 3
if x % 3 == 0:
    print("số bước tối thiểu để rùa di chuyển đến x la: ", a)
else:
    print("số bước tối thiểu để rùa di chuyển đến x là: ", a + 1)
