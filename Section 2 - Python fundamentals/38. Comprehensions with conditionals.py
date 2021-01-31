# https://blog.tecladocode.com/python-list-comprehensions-conditionals/
# https://blog.tecladocode.com/python-30-day-20-map-filter/


ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# This lower cases the lists and then finds those values in both lists using intersection

#  friends_lower = set([f.lower() for f in friends])
#  guests_lower = set([g.lower() for g in guests])
#  print(friends_lower.intersection(guests_lower))

friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)
