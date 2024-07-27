s1 = input("s1 = ")
s2 = input("s2 = ")
# in ra chuỗi s1 đảo ngược 
print("sau khi đảo ngược s1 = ", s1[::-1])
#Nhập vào 2 số nguyên a, b (1 <=a < b <= len(s2)). In ra chuỗi s2 sau khi đảo ngược chuỗi từ vị trí a đến b.
a = int(input("a = "))
b = int(input("b = "))
if 1 <= a < b <= len(s2):
    chuỗi_ab = s2[a:b+1]
    chuỗi_ab_đảo = chuỗi_ab[::-1]
    s2 = s2[:a] + chuỗi_ab_đảo + s2[b+1:] 
print("Sau khi đảo s2 = ", s2)
#In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn
s3 = " "
for i in range(len(s1)):
    if i % 2 != 0:
        s3 += s1[i]
print("s3 = ", s3)
#Trả về chuỗi s4 là đan xen các kí tự của s1 và s2
s4 = ""
len_s1 = len(s1)
len_s2 = len(s2)
min_len = min(len_s1, len_s2)
for i in range(min_len):
    s4 += s1[i] + s2[i]
if len_s1 > len_s2:
    s4 += s1[min_len:]
else:
    s4 += s2[min_len:]
print("Chuỗi s4 là đan xen các ký tự của s1 và s2:", s4)
# Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi và in ra kết quả
if len(s1) < 2 or len(s2) < 2:
    print("Cả hai chuỗi cần có ít nhất 2 ký tự.")
else:
    new_s1 = s2[:2] + s1[2:]
    new_s2 = s1[:2] + s2[2:]
    print("Chuỗi s1 sau khi đổi chỗ 2 ký tự đầu tiên:", new_s1)
    print("Chuỗi s2 sau khi đổi chỗ 2 ký tự đầu tiên:", new_s2)