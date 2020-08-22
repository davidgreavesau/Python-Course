# https://blog.tecladocode.com/destructuring-in-python/
# https://blog.tecladocode.com/python-30-day-9-enumerate-zip/

# Gets first value and puts it in usd and second value into eur
# This is called destructuring
currencies =  (0.8, 1.2)
usd, eur = currencies

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for name , age in friends:
    print(f"{name} is {age} years old.")

example_list = ["A", "B", "C", "D"]

for counter, letter in enumerate(example_list):
    print(counter , letter)

head, *tail = [1, 2, 3, 4, 5, 6]

print(head)
print(tail)


*head, tail = [1, 2, 3, 4, 5, 6]

print(head)
print(tail)