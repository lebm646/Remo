
from database import db
from movie_dict import genre_list

# print out menu option
def cli_menu():
    print("Choose one of the following options:\n")
    print("1. Search movies by genre")
    print("2. Search by rating")
    print("3. Search by duration")
    print("4. Exit\n")

    choice = input("Enter option: ")
    return choice


# print out all the genres that are available
def print_genres():
    print('You can seach for movies with certain genres')
    print("We have these following genres:")
    for genre in genre_list:
        print(genre)

# take in one or more genres and search for movies that fit all the genre
def search_by_genre():
    print_genres()
    genres = input("Enter genres (comma-separated) to find movies: ")

    genres = [genre.strip().lower() for genre in genres.split(",")]

    results = [movie for movie in db.movies 
            if all(genre in map(str.lower, movie.genres) for genre in genres)]
    
    return results

# take in min and max duration and find movies based on that info
def search_by_duration():
    min_duration = float(input("Enter the minimum duration you want in minutes: "))
    max_duration = float(input("Enter the maximum duration you want in minutes: "))

    results = [movie for movie in db.movies if min_duration <= movie.duration <= max_duration]
    return results

# find movies with same or higher input rating
def search_by_rating():
    min_rating = float(input("Enter the minimum rating you want: "))
    results = [movie for movie in db.movies if movie.rating >= min_rating]
    return results

# take in a list of found movies and print out 
def print_results(results):
    results = sort_movies(results)
    
    if results:
        print("\nMovies found:")
        for movie in results:
            print(movie)
    else:
        print("Sorry! No movies found for the specified criteria.\n")

# sort movies
def sort_movies(movies):
    if not movies:
        return movies

    sort_choice = input("Sort by (1) Rating or (2) Duration? ")
    if sort_choice == "1":
        return sorted(movies, key=lambda movie: movie.rating, reverse=True)
    elif sort_choice == "2":
        return sorted(movies, key=lambda movie: movie.duration)
    else:
        print("Invalid choice. Returning unsorted results.")
        return movies

        

        
