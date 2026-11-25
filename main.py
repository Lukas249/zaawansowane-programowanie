from fastapi import FastAPI
from sqlalchemy import select

from session_db import get_session
from tables_db import Movie, Link, Rating, Tag

app = FastAPI()

def get_all(class_type):
    with get_session() as session:
        return session.scalars(select(class_type)).all()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/movies")
def read_movies():
    return [movie.__dict__ for movie in get_all(Movie)]


@app.get("/links")
def read_links():
    return [link.__dict__ for link in get_all(Link)]


@app.get("/ratings")
def read_ratings():
    return [rating.__dict__ for rating in get_all(Rating)]


@app.get("/tags")
def read_tags():
    return [tag.__dict__ for tag in get_all(Tag)]