# a,Viết một chương trình yêu cầu người dùng nhập một số nguyên dương. Tính và in ra tổng các chữ số của số đó. Ví dụ: Đối với số 12345, tổng các chữ số là 1 + 2 + 3 + 4 + 5 = 15.
'''a = int(input("a = "))
while a <= 0:
    print("Nhap a nguyen duong: ")
    a = int(input("a = "))
print("Số nguyên dương a vừa nhập la: ", a)
sum = 0
while a % 10 != 0:
    sum += a % 10
    a //= 10
print("sum = ", sum)'''
# b,Tính tổng các ước số của một số nguyên dương: Viết một chương trình yêu cầu người dùng nhập một số nguyên dương n. Tính và in ra tổng của tất cả các ước số của n. Ước số của một số là các số mà chia hết cho số đó mà không dư. Ví dụ: Ước số của 6 là 1, 2, 3, và 6.
'''n = int(input("n = "))
while n <= 0:
    print("Nhập n: ")
    n = int(input("n = "))
print("n = ", n)
sum = 0
for i in range(1, n+1):
    if n % i == 0: 
        sum += i
print("Tổng các ước số là: ", sum)'''
# c,Kiểm tra tam giác: Viết chương trình yêu cầu người dùng nhập vào 3 số nguyên dương. Kiểm tra xem 3 số đó có tạo thành tam giác hay không? Nếu có thì đó là tam giác gì?(Cân, đều, vuông, nhọn, tù)
print('nhap a, b, c : ')
a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b :
    if a == b == c : 
        print('tam giac deu')
    elif a == b != c :
        print('tam giac can')
    elif a*a > b*b + c*c and b*b > a*a + c*c and c*c > a*a + b*b :
        print('tam giac tu')
    elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b :
        print('tam giac vuong')
    else :
        print('tam giac nhon')
else :
    print('khong the tao thanh tam giac')

