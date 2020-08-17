art_friends = {"Rolf", "Anne" , "Jenn"}
science_friends = {"Jenn", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print("Art Only: " + str(art_but_not_science))
print("Science Only: " + str(science_but_not_art))

not_in_both = art_friends.symmetric_difference(science_friends)
print("Not in both: " + str(not_in_both))

art_and_science = art_friends.intersection(science_friends)
print("In Both: " + str(art_and_science))

all_friends = art_friends.union(science_friends)
print("All Friends: " + str(all_friends))

new_friend = input("What is a name of a friend: ")
