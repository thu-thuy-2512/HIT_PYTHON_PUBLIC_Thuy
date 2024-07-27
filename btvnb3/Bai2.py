k = int(input("k = "))
a = [int(input(f"a[{i}] = ")) for i in range(k)]
print("a = ", a)
n = int(input("Nhập số dòng n = "))
m = int(input("Nhập số cột m = "))
if n * m > k:
    print("NO")
else:
    x = []
    dem = 0
    for i in range(n):
        cột = a[dem : dem + m]
        x.append(cột)
        dem += m
    print("Ma trận x(", n, "x", m, ") là: ")
    for cột in x:
        print(cột)    
