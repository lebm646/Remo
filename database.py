from movie_dict import movie_dict

class Movie:
    def __init__(self, title, genres, duration, rating):
        self.title = title
        self.genres = genres #List of genres e.g. ["Action", "Thriller"]
        self.duration = duration # in minutes
        self.rating = rating # out of 10

    def __repr__(self):
        return (
        '\n'
        f"{self.title}\n"
        f"Genre: {', '.join(self.genres)}\n"
        f"Duration: {self.duration} min\n"
        f"Rating: {self.rating}/10"
        '\n'
    )

class Database:
    def __init__(self, movie_dict):
        self.movies = []

        for movie_data in movie_dict:
            movie = Movie(movie_data['title'], movie_data['genres'], movie_data['duration'], movie_data['rating'])
            self.add_movie(movie)
        
    def add_movie(self, movie):
        self.movies.append(movie)
    
db = Database(movie_dict)

