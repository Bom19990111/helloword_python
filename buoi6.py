def information_student(**sv):
    if "hoten" in sv.keys():
        print("Họ tên: {}".format(sv["hoten"]))
    if "ngaythangnamsinh" in sv.keys():
        print("Ngày tháng năm sinh: {}".format(sv["ngaythangnamsinh"]))
    if "diachi" in sv.keys():
        print("Địa chỉ: {}".format(sv["diachi"]))
    if "namsinh" in sv.keys():
        tuoi = 2021 - sv["namsinh"]
        print("Tuổi: {}".format(tuoi))
        


        
# information_student(hoten = "Thịnh", ngaythangnamsinh = "20-11-2021", diachi = "20 Tp Hue")
# information_student(hoten = "Nam", diachi = "", namsinh = 2000)

# def hello(name = "Thinh"):
#     print(f"hello {name}")
# hello()
# hello(name = "Nam")

# def list_student(dssv):
#     for sv in dssv:
#         print(f"Hello {sv}")
# dssv=["nam", "Khánh", "An"]
# list_student(dssv)

# x = lambda a: a / 2022
# print("Kết quả bài 1: " + str(x(2000)))
# y = lambda x,y,z: (x + y)/ z
# print("Kết quả bài 2: " + str(y(4,6,5)))

def luythua(n):
    c = lambda x: x**n
    return c
tinhmu = luythua(4)
y = tinhmu(2)
print(y)