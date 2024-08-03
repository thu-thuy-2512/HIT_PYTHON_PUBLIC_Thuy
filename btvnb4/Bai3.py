n , m = map(int, input().split())
mang = list(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happy = 0

for i in mang:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1

print(f"Tổng mức độ hạnh phúc là: {happy}")