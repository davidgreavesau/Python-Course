# https://blog.tecladocode.com/python-enumerate/

friends = ["Rolf" , "John", "Anna"]
counter = 0

for f in friends:
    print(counter)
    print(f)
    counter = counter + 1

# this is the same code but using enumerate. Start is setting the start value
for counter, friend in enumerate(friends, start=1):
    print(f" Count: {counter}  Friend: {friend}")

print(list(enumerate(friends)))
print(dict(enumerate(friends)))

