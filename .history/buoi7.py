class Student:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def cvStudent(self):
        print(
            f"Học sinh: {self.name}, Tuổi: {2021 - self.age}, Quê quán: {self.country}")

# Lớp Class kế thừa Student
class Class(Student):
    def __init__(self, name, age, country, classname):
       super().__init__(name, age, country) #Kế thừa
       self.classname = classname
    def ClassInSchool(self):
        print(f"Lớp: {self.classname}")


student = Class("Trần Nhật Thịnh", 2000, "Huế - Việt Nam", "CNTT-K17")
student.cvStudent()
student.ClassInSchool()
