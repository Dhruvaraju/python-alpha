class Student:
    def __init__(self):
        self.name ="dexter"
        self.standard =12
        self.marks=[89,86,84,96,90]
    
    def average(self):
        return sum(self.marks)/len(self.marks)


student = Student()
print(Student.average(student))
print(student.average())