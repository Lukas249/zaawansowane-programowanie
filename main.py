from fastapi import FastAPI
from pydantic import BaseModel

from load_data import load_file

app = FastAPI()


class Movie(BaseModel):
    movieId: int
    title: str
    genres: str


movies = load_file("database/movies.csv")

for i in range(len(movies)):
    movies[i] = Movie(**movies[i])


class Link(BaseModel):
    movieId: int
    imdbId: str
    tmdbId: str


links = load_file("database/links.csv")

for i in range(len(links)):
    links[i] = Link(**links[i])


class Rating(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int


ratings = load_file("database/ratings.csv")

for i in range(len(ratings)):
    ratings[i] = Rating(**ratings[i])


class Tag(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int


tags = load_file("database/tags.csv")

for i in range(len(tags)):
    tags[i] = Tag(**tags[i])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movies")
def read_movies():
    return movies


@app.get("/links")
def read_links():
    return links


@app.get("/ratings")
def read_ratings():
    return ratings


@app.get("/tags")
def read_tags():
    return tags
