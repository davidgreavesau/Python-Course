# https://blog.tecladocode.com/python-30-day-6-for-loops/

friends = ["Rolf", "Jen", "Anne" ]

for friend in friends:
    print(friend)


elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for _ in elements:
    print(_)

# This will run 10 times
for _ in range(10):
    print("Hello, World")

# This will print the numbers 5 to 10
for _ in range(5, 10):
    print(_)

# This gives you the numbers 2 to 19, but only every third one
for _ in range(2, 20, 3):
    print(_)

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}")