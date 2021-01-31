friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {f.lower() for f in friends}
guests_lower = {g.lower() for g in guests}

# This is set comprehension. It will remove duplicate entries
present_friends = friends_lower.intersection(guests_lower)
present_friends = {name.title() for name in present_friends}
print(present_friends)


friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)