my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number

print(f"You got it right: {matches}.")

print(5 > 10)
print(5 < 10)
print(10 > 10)
print("A" < "a")

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)