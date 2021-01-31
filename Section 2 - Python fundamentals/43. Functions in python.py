# https://blog.tecladocode.com/python-30-day-12-functions/

def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


greet()


def get_even_numbers():
    for number in range(1, 11):
        print(number *2)


get_even_numbers()