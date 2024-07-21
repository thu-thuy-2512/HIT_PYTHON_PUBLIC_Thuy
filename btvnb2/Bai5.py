'''n = int(input("n = "))
def kt(n):
    sum = 0
    while n > 0:
        a = n % 10
        sum += a * a * a
        n //= 10
        return n == sum
for i in range(1, n + 1):
    if kt(i):
        print(i)'''
n = int(input("Nhập n: "))
for i in range(1, n + 1):
  sum = 0
  n = i
  while n > 0:
    b = n % 10
    sum += b * b * b
    n //= 10
  if i == sum:
    print(i)
