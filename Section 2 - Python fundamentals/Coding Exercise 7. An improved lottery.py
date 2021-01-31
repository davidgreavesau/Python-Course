import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

top_player = players[0]

for player in players:
    matching_numbers = player["numbers"].intersection(lottery_numbers)
    number_matching = len(matching_numbers)

    if number_matching > len(top_player["numbers"].intersection(lottery_numbers)):
        top_player = player

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

numbers_matched = len(top_player["numbers"].intersection(lottery_numbers))
winnings = 100 ** numbers_matched
print(f"Numbers matched: {numbers_matched}")
print(f"{top_player['name']} won {winnings}.")