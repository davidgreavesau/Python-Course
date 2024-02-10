# https://www.youtube.com/watch?v=W7QByFjVom8

my_file = open('Section 6 - Files in Python/files_project/data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('Section 6 - Files in Python/files_project/data.txt', 'w')

my_file_writing.write(user_name)

my_file_writing.flush()
my_file_writing.close()