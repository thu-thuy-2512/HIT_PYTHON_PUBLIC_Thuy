n = int(input("n = "))
while n <= 0:
    print("Nhập số nguyên dương n = ")
    n = int(input())
print("Số nguyên dương vừa nhập là: ", n)
s1 = 0
s2 = 1
if n >= 2:
    print(s1, s2, end=' ')
elif n == 1:
    print(s1)
for i in range(n - 2) : 
    sn = s1 + s2
    s1 = s2
    s2 = sn
    print(sn, end=' ')
    
