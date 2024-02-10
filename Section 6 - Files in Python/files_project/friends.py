# Ask the user for a list of three friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'


friends = input('Enter the name for three friends, separated by commas (no spaces): ').split (',')
# ['Steve', 'John', 'Dave']


people_file = open('Section 6 - Files in Python/files_project/people.txt', 'r')
people_nearby = [line.strip() for line in people_file.readlines()] # [line1, line2, line3, line4]

people_file.close()


friends_set = set(friends)
people_nearby_set = set(people_nearby)

# Get the matching names
friends_nearby_set = friends_set.intersection(people_nearby_set)


nearby_friends_file = open('Section 6 - Files in Python/files_project/nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Catch up with them for a beer.')
    nearby_friends_file.write(f'{friend}\n')


nearby_friends_file.flush()
nearby_friends_file.close()