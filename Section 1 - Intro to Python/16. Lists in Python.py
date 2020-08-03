friends = [
    ["Rolf", 23],
    ["Bob", 55],
    ["Anne", 21],
    ["Steve", 43]
]

print("length: " + str(len(friends)))

print(friends[0][0])
print(friends[1][1])


other_friends = ["John", "Peter", "Neil"]
other_friends.append("Dave")
other_friends.remove("Peter")
print(other_friends)

print(friends)
friends.remove(["Bob", 55])
print(friends)


l_1 = [1, 2, 3, 4]
l_2 = [5, 6, 7, 8]

l_1.extend(l_2)
print(l_1)