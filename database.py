from movie import Movie
from movie_dict import movie_dict

class Database:
    def __init__(self, movie_dict):
        self.movies = []
        for movie_data in movie_dict:
            movie = Movie(movie_data['title'], movie_data['genres'], movie_data['duration'], movie_data['rating'])
            self.movies.append(movie)
        
    def add_movie(self, movie):
        self.movies.append(movie)

    # search movies based on input genres
    def get_movie_by_genres(self, genres):
        if isinstance(genres, str):
            genres = [genre.strip().lower() for genre in genres.split(",")]

        return [movie for movie in self.movies 
                if all(genre in map(str.lower, movie.genres) for genre in genres)]

    # search movies based on input duration
    def get_movies_by_duration(self, min_duration=0, max_duration=float('inf')):
        return [movie for movie in self.movies if min_duration <= movie.duration <= max_duration]
    
    # search movies based on rating
    def get_movies_by_rating(self, min_rating=0.0):
        return [movie for movie in self.movies if movie.rating >= min_rating]


    

db = Database(movie_dict)

