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
