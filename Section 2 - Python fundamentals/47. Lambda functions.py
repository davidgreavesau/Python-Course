# https://blog.tecladocode.com/python-30-day-16-lambda-expressions/

# def divide(x, y):
#    return(x / y)

# Lambda function
divide = lambda x, y: x / y
print(divide(15, 3))

def average(sequence):
    return sum(sequence) / len (sequence)

# lambda version
# average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))