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


euclidean_division = divmod(5, 2)
print(euclidean_division)


raw_time = 8594
minutes, seconds = divmod(raw_time,60)
hours, minutes = divmod(minutes,60)

print(f"{raw_time}s is {hours}h {minutes}m {seconds}s")

row_number = 235
result = row_number % 2
print(result)


    