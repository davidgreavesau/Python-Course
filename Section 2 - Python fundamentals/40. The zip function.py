# https://blog.tecladocode.com/python-zip/
# https://blog.tecladocode.com/python-zip_longest/
# https://blog.tecladocode.com/python-30-day-9-enumerate-zip/

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends, time_since_seen))
print(long_timers)


names = ["John", "Anne", "Peter"]
ages = [26, 31, 29]

for name, age in zip(names,ages):
    print(f"{name} is {age} years old.")