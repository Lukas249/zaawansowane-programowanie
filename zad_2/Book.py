from zad_2.Library import Library


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int) -> None:
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"""Book[
            Library: {self._library}
            Publication Date: {self._publication_date}
            Author: {self._author_name} {self._author_surname}
            Number of Pages: {self._number_of_pages}
        ]"""
