from fastapi import FastAPI
from load_data import load_file

app = FastAPI()


class Movie:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId: str, movieId: str, rating: float, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.rating = float(rating)
        self.timestamp = int(timestamp)


class Tag:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = int(timestamp)


movies = [Movie(*row) for row in load_file("database/movies.csv")]
links = [Link(*row) for row in load_file("database/links.csv")]
ratings = [Rating(*row) for row in load_file("database/ratings.csv")]
tags = [Tag(*row) for row in load_file("database/tags.csv")]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movies")
def read_movies():
    return [movie.__dict__ for movie in movies]


@app.get("/links")
def read_links():
    return [link.__dict__ for link in links]


@app.get("/ratings")
def read_ratings():
    return [rating.__dict__ for rating in ratings]


@app.get("/tags")
def read_tags():
    return [tag.__dict__ for tag in tags]
