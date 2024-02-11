import json

file = open('Section 6 - Files in Python/files_project/friends_json.txt', 'r')
file_contents = json.load(file) # Reads file and turns to dictionary

file.close()

print(file_contents['friends'][0])


cars = [
    { 'make': 'Ford', 'model': 'Fiesta'},
    { 'make': 'Ford', 'model': 'Focus'},
    { 'make': 'Holden', 'model': 'Commodore'}
]

car_file = open('Section 6 - Files in Python/files_project/cars_json.txt', 'w')
json.dump(cars,car_file,indent = 6) # Writes the dictionary to the file
car_file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
print(incorrect_car[0]['released'])
