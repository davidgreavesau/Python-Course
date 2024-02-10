csv_file= open('Section 6 - Files in Python/files_project/csv_data.txt', 'r')
lines = csv_file.readlines()
csv_file.close()

# This is getting part of the list from index 1 onwards and removing white space
lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1].capitalize()
    university = person_data[2].title()
    degree = person_data[3]

    print(f'{name} is {age} studying {degree} at {university}.')


sample_csv_value = ','.join(['Dave', '55', 'USQ', 'Surveying'])
print(sample_csv_value)