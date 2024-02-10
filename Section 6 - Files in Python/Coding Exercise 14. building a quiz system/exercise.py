

# read from questions.txt and append each line into a list
questions= open('Section 6 - Files in Python\Coding Exercise 14. building a quiz system/questions.txt', 'r')


# read all lines and get rid of line break for each line, then append each stripped line to a list
question_list = [line.strip() for line in questions]
questions.close()

score = 0  # initialize score
question_count = 0 # question count
total = len(question_list)  # set total score


for line in question_list:

    question_count += 1

    # split equation with `=` into question and answer
    question, answer = line.split("=")
 
    # print question and wait for user to input their answer
    input_answer = input(f"Question {question_count}: {question}=")
 
    if answer == input_answer:  # if user input matches answer
        score += 1  # increase score


result = open("Section 6 - Files in Python\Coding Exercise 14. building a quiz system/result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()