from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movies"

    movieId: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    genres: Mapped[str] = mapped_column(String)


class Link(Base):
    __tablename__ = "links"

    movieId: Mapped[str] = mapped_column(String, primary_key=True)
    imdbId: Mapped[str] = mapped_column(String)
    tmdbId: Mapped[str] = mapped_column(String)


class Rating(Base):
    __tablename__ = "ratings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    userId: Mapped[str] = mapped_column(String)
    movieId: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[int] = mapped_column(Integer)


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    userId: Mapped[str] = mapped_column(String)
    movieId: Mapped[str] = mapped_column(String)
    tag: Mapped[str] = mapped_column(String)
    timestamp: Mapped[int] = mapped_column(Integer)
