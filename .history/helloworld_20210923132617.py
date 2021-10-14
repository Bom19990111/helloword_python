import random #import hàm random

fullname = input('Nhập tên sinh viên: ');
birthdate = input('Nhập ngày sinh sinh viên: ');
score = float(input('Nhập điểm quá trình sinh viên: '));
daily_score = float(input('Nhập điểm thi sinh viên: '));

sbd = "PXU"+str(random.randint(1,99))
if random.randint(1,99) == 1:
    "PXU" + "0" + sbd
else: 
    "PXU" + sbd
    
print("Họ và tên:", fullname)
print("Mã sv:", str(sbd))
print("Ngày sinh:", birthdate)
print("Điểm thi:", daily_score)
print("Điểm quá trình:", score)
print("Điểm tổng kết", str((score +daily_score)/2))