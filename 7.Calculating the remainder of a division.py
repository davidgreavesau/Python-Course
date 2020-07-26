interger_division = 13 // 5
print(interger_division)

#gets the modulus. Remainder
remainder = 13 % 5
print(remainder)


x = 37
remainder = x % 2
print(remainder)

def euclidean_division(x, y):
    quotient = x // y
    remainder = x % y
    print("euclideon division")
    print(f"{quotient} remainder {remainder}")

euclidean_division(10, 3) # 3 remainder 1
euclidean_division(11, 3) #3 remainder 2

euclidean_division(10, -3)

    