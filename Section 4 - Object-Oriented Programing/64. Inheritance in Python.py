class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len (self.marks)


# This class is a child of student. It extends it.
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # This calls the parent classes init method
        super().__init__(name, school)
        self.salary = salary
    
    # change a simple no arguement method into a property.
    # do not use this if you are performing an action
    @property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)

rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())

print(rolf.weekly_salary)