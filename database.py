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
        
    def get_movie_by_genres(self, genres):
        if isinstance(genres, str):
            genres = [genre.strip() for genre in genres.split(",")]

        return [movie for movie in self.movies 
                if all(genre in movie.genres for genre in genres)]
    

db = Database(movie_dict)

