age = 3436
age_as_str = str(age)
print(f"You are {age}")

name = "Dave"
greeting = f"How are you, {name}"
print(greeting)

name = "dave"
final_greeting = "How are you, {}?"
dave_greeting = final_greeting.format(name)
print(dave_greeting)

x = 4863.4343091
print(f"The number is {x:.6}")
print(f"The number is {x:.3}")
print(f"The number is {x:.4f}")

y = 1000000000000000
print(f"{y:,}")
print(f"{y:_}")5

questions = 30
correct_answers = 23
print(f"You got {correct_answers / questions : .2%} correct!!")

number_of_files = 4

for file_number in range(1, number_of_files + 1):
    print(f"image{file_number:03}.png")


number_of_files = 3
number_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
	print(f"image{file_number:0{number_digits}}.png")