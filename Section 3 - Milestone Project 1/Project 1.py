
MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


# Function for adding a movie
def add_a_movie():

    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    # This appends the movie details to the dictionary
    movies.append({
     'title': title,
      'director': director,
       'year': year
    })


# Function for printing movies
def print_movies():
    for movie in movies:
        print_movie_info(movie)


# Function for getting movie details and then printing it.
def print_movie_info(movie):
    title = movie["title"]
    director = movie["director"]
    year = movie["year"]

    print(f"Title: {title}")
    print(f"Director: {director}")
    print(f"Year: {year}")


# Function for finding movies
def find_a_movie():
    search_title = input("Enter the movie title you're looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie_info(movie)


# This dictionary will act like an if statement
user_options = {
    "a": add_a_movie,
    "l": print_movies,
    "f": find_a_movie
}


# And another function here for the user menu
def user_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again...')

        selection = input(MENU_PROMPT)

user_menu()
