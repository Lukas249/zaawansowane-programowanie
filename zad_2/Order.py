from typing import List

from zad_2.Book import Book
from zad_2.Employee import Employee
from zad_1.Student import Student


class Order:
    def __init__(self, employee: Employee, student: Student, books: List[Book], order_date: str) -> None:
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        order_str = f"""Order[
            Employee: {self._employee}
            Student: {self._student}
            Books:
        """

        for book in self._books:
            order_str += str(book) + "\n"

        order_str += f"""
            Order Date: {self._order_date}
        ]"""

        return order_str
