
list_class = []

for i in range(5):
    hoten = input("Nhập họ tên thứ " +str(i)+ ": ")
    list_class.append(hoten)
    print(list_class)

vitri = int(input("Nhập vị trí cần sửa: "))
hotenmoi =  input("Nhập họ tên mới: ")
list_class[vitri] = hotenmoi

print(list_class)