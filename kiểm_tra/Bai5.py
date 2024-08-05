n = int(input("n = "))
while n < 1 or n > 100:
    n = int(input("n = "))
print("Số lượng phần tử trong dãy n = ", n)
a = []
for _ in range(0, 10^9):
    num = int(input(f"Nhập phần tử {_ + 1}: "))
    a.append(num)
print("a = ", a)