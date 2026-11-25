from sqlalchemy import select

from load_file import load_file
from session_db import get_session, get_engine
from tables_db import Base, Movie, Link, Rating, Tag

SessionLocal = get_session()


def init_db():
    Base.metadata.create_all(bind=get_engine())

    with SessionLocal() as session:
        if session.scalars(select(Movie)).first() is not None:
            return

        movies = [
            Movie(movieId=row[0], title=row[1], genres=row[2])
            for row in load_file("database/movies.csv")
        ]
        links = [
            Link(movieId=row[0], imdbId=row[1], tmdbId=row[2])
            for row in load_file("database/links.csv")
        ]
        ratings = [
            Rating(
                userId=row[0],
                movieId=row[1],
                rating=float(row[2]),
                timestamp=int(row[3]),
            )
            for row in load_file("database/ratings.csv")
        ]
        tags = [
            Tag(
                userId=row[0],
                movieId=row[1],
                tag=row[2],
                timestamp=int(row[3]),
            )
            for row in load_file("database/tags.csv")
        ]

        session.add_all(movies)
        session.add_all(links)
        session.add_all(ratings)
        session.add_all(tags)

        session.commit()

init_db()