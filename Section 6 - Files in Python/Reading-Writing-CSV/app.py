import csv

# Dictionary
movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "Farrelly"},
    {"name": "Amadeus", "director": "Forman"}
]

def write_to_file(output):
    with open("Section 6 - Files in Python/Reading-Writing-CSV/file.csv", "w") as f:
        writer = csv.writer(f,lineterminator='\n')
        f.write("name,director\n")
        writer.writerows([elem.values() for elem in output])


def write_to_file_dict(output):
    with open("Section 6 - Files in Python/Reading-Writing-CSV/file.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "director"], lineterminator='\n')
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open("Section 6 - Files in Python/Reading-Writing-CSV/file.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            print(f"Name: {line[0]}\tDirector: {line[1]}")

def read_from_file_dict():
    with open("Section 6 - Files in Python/Reading-Writing-CSV/file.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']}\tDirector: {line['director']}")


def read_from_file_dict_to_list():
    with open("Section 6 - Files in Python/Reading-Writing-CSV/file.csv", "r") as f:
        reader = csv.DictReader(f)
        print(list(reader))
        return list(reader)

# write_to_file(movies)
            
# write_to_file_dict(movies)
            
read_from_file_dict_to_list()