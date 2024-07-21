'''n = int(input("n = "))
while n <= 1:
    print("Nhập lại n = ")
    n = int(input())
print("n = ", n)
sum = 0
for i in range(1, n // 2 + 1 ):
    if n % i == 0:
        sum += i
        for i in range(1, n // 2):
            if sum == n and sum != i:
                print(i)'''
'''def check(a):
  """Kiểm tra xem một số có phải là số hoàn hảo hay không."""
  sum = 0
  for i in range(1, a // 2 + 1):
    if a % i == 0:
      sum += i
  return sum == a and sum != 0

n = int(input("Nhập n: "))

for i in range(1, n + 1):
  if check(i):
    print(i, "là số hoàn hảo")

if not any(check(a) for a in range(1, n + 1)):
  print("Không tìm thấy số hoàn hảo nào trong khoảng từ 1 đến", n)'''
def tim_uoc(n) : 
    sum = 0
    for i in range(1, n // 2 + 1) :
        if (n % i == 0) : 
            sum += i
    return sum == n
n = int(input('nhap n : '))
for i in range(1, n + 1) :
    if tim_uoc(i) : 
        print(i, "là số hoàn hảo\n", end=' ')
