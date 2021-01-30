# https://blog.tecladocode.com/python-list-comprehensions/
# https://blog.tecladocode.com/python-30-day-15-comprehensions/

numbers = [0, 1, 2, 3, 4 ,5]

double_numbers = [number * 2 for number in numbers]
print(double_numbers)

# This is the same but using range
double_numbers = [number * 2 for number in range(6)]
print(double_numbers)


friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]
print(age_strings)


names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

friend = input("Enter your friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]


# title() turns into title casing

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends")