a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
c = int(input('Nhập số c: '))
max = a
if(b > max):
    max = b
    print("Số lớn nhất là:" + str(b))
elif(c > max):
    max = c
    print("Số lớn nhất là:" + str(c))
else:
    print("Số lớn nhất là:" + str(a))
    