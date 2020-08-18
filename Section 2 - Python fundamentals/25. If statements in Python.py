# https://blog.tecladocode.com/python-30-day-5-conditionals-booleans/
# https://blog.tecladocode.com/python-30-day-5-conditionals-booleans/

friend = "Rolf"
user_name = input("Enter your name: ")

#Python relies on the 4 spaces to know where the if statement is
#This is a compound if statement / if statement with two branches
if user_name == friend:
    print("Hello, friend!")
else:
    print("Sorry I don't know you...")


print(bool(5)) #this is true

name = input("Enter your name again: ")

print (bool(name))

if name:
    print("We know your name...")


friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your username: ")

if user_name in friends:
    print("Hello my friend...")

elif user_name in family:
    print("Hello, family!")
    
else:
    print("I don't know you...")
