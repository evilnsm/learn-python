class Student:
    def __init__(self,a,b,c):
        self.name = a
        self.age = b
        self.score = c

stu = Student('Bob',20,88)

stu2=Student()


print stu.__dict__

print stu2.__dict__

print Student.__dict__
