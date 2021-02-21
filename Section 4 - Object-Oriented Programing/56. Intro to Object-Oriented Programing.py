my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': None # something here
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

class Student:
    #dunder method
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    # These are methods. A function inside a class.
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def print_info(self):
        print(f"Name: {self.name} Grades: {self.grades}")
    

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.average())
print(student_one.grades)