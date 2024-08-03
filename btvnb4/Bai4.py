n = 5
setA = {1 , 2, 3, 4, 5}
maxSum = 7

setNew = sorted(setA)

setCon = set()
sum = 0

for i in setNew:
    if sum + i <= maxSum:
        setCon.add(i)
        sum += i
    else:
        break
print(setCon)