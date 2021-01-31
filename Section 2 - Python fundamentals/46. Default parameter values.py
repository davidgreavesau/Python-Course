
# y = 3 is a default parameter
# all parameters after a default value must be defined as well

def add(x, y=3):
    total = x + y
    return total

# Prints 15
print(add(5, 10))

# Prints 8
print(add(5))

# Prints 8
print(add(x=3))

# Prints 7
print(add(x=5, y=2))


print(1, 2, 3, 4, 5, sep=" - ")

