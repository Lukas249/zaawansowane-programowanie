from fastapi import FastAPI
from pydantic import BaseModel

from load_data import load_file

app = FastAPI()


class Movie(BaseModel):
    movieId: str
    title: str
    genres: str


movies_columns, movies = load_file("database/movies.csv")

for i in range(len(movies)):
    movies[i] = Movie(**dict(zip(movies_columns, movies[i])))


class Link(BaseModel):
    movieId: str
    imdbId: str
    tmdbId: str


links_columns, links = load_file("database/links.csv")

for i in range(len(links)):
    links[i] = Link(**dict(zip(links_columns, links[i])))


class Rating(BaseModel):
    userId: str
    movieId: str
    rating: float
    timestamp: int


ratings_columns, ratings = load_file("database/ratings.csv")

for i in range(len(ratings)):
    ratings[i] = Rating(**dict(zip(ratings_columns, ratings[i])))


class Tag(BaseModel):
    userId: str
    movieId: str
    tag: str
    timestamp: int


tags_columns, tags = load_file("database/tags.csv")

for i in range(len(tags)):
    tags[i] = Tag(**dict(zip(tags_columns, tags[i])))


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
