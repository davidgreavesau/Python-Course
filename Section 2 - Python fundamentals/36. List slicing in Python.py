# https://blog.tecladocode.com/python-slices/
# https://blog.tecladocode.com/python-slices-part-2/
# https://blog.tecladocode.com/python-quick-sequence-reversal/

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

# All of the list after the first one
print(friends[1:])

# All of the list before the 4th one
print(friends[:4])

# This gives you a new list 
print(friends[:])

# This gives the list from the 3rd last item
print(friends[-3:])

# This gives the list except the last 2
print(friends[:-2])

slice_instance = slice(0, 2)
x = [1, 2, 3, 4, 5]

x_slice = x[slice_instance]
print(x_slice) # [1, 2]

s = slice(1,4)

t = (1, 2, 3, 4, 5) # tuple
l = [1, 2, 3, 4, 5] # list
c = "12345" # string

print(t[s])
print(l[s])
print(c[s])
