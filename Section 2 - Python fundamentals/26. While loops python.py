# https://blog.tecladocode.com/python-30-day-8-while-loops/

is_learning = True

while is_learning:
    print("You're learning!")
    user_input = input("Are you learning? ")
    is_learning = user_input == "yes"


user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program (yes/no): ")

print("We stopped running....")