# a.
'''sum = 0
n = int(input("n = "))
while n <= 0:
    print("n = ")
    n = int(input("nguyên dương n = "))
print("n = ", n)
for i in range(1, 2*n + 2):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print("sum = ", sum)'''
# b
'''n = int(input("n = "))
sum = 1
M = 1
for i in range(1, n + 1):
    M = M + i
    sum += 1/M
print(sum)'''
# c
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a == 0:
    print("Không phải phương trình bậc 2")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b // 2 * a
        print("Phương trình có nghiệm duy nhất x1 = x2 =", x)
    else:
        x1 = (-b + delta ** (1/2)) // 2 * a
        x2 = (-b - delta ** (1/2)) // 2 * a
        print("Phương trình có 2 nghiệm phân biệt: x1 = ", x1, " \n x2 = ", x2)