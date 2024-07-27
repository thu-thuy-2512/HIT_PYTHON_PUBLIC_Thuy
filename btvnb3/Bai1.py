N = int(input("N = "))
list = [int(input(f'list[{i}] = ')) for i in range(N)]
print("list = ", list)
X = int(input("X = "))
print(f'{X} xuất hiện', list.count(X), 'lần')
replace = [8, 5, 4, 0, 1, 3]
list[1:7] = replace
print(list)
print("Max = ", max(list))
print("Min = ", min(list))
Y = int(input("Y = "))
list.insert(0, Y)
print(f"list sau khi chèn {Y} vào đầu list là: ", list)
def check_sort(list):
    if list == sorted(list):
        print("TĂNG")
    elif list == sorted(list, reverse = True):
        print("GIẢM")
    else:
        print("NO")
check_sort(list)
my_list2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
print("Sắp xếp theo thứ tự tăng dần: ", sorted(my_list2, reverse = False))
my_list2 = [abs(i) for i in my_list2]
print("Sắp xếp theo thứ tự tăng dần giá trị tuyệt đối: ",sorted(my_list2, reverse= False))

