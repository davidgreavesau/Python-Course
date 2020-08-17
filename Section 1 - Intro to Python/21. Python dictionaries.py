# https://blog.tecladocode.com/python-updating-dictionaries/
# https://blog.tecladocode.com/python-30-day-10-dictionaries/

friend_ages = {"Rolf": 24, "Adam" : 30, "Anne" : 27}
print(friend_ages["Rolf"])

#Assigning value to a key
friend_ages["Bob"] = 20
friend_ages["Rolf"] = 25
print(friend_ages)

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

friends_two = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friends_ages = dict(friends_two)
print(friends_ages)