class Student:
    def __init__(self,name,standard,marks):
        self.name =name
        self.standard =standard
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    def __str__(self):
        return f"{self.name} is {self.standard}th std and has average {self.average()}"
    def __repr__(self):
        return f"{self.name} is {self.standard}th std and has average {self.average()}"

student = Student("dexter",12,[89,86,84,96,90])
print(Student.average(student))
print(student.average())

# Once after creating str method when we call the student class it will print the return of str method
print(student)

# If str function is not present and a repr method is present it will return the return of repr method
# repr is generally used to print the object in the console
# str is used for printing the object in the file