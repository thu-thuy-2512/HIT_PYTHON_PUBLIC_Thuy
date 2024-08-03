n = int(input())
lst = []
for i in range(n):
    lst.append(input())

tpl = tuple(int(x) for x in lst)

sum = 0
for i in tpl:
    sum += i
print(sum / n)