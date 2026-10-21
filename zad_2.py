from typing import List

from zad_1 import Student


class Library:

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self):
        return f"""Library[
            City: {self._city}
            Street: {self._street}
            Zip Code: {self._zip_code}
            Opening Hours: {self._open_hours}
            Phone: {self._phone}
        ]"""


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f"""Employee[
            First Name: {self._first_name}
            Last Name: {self._last_name}
            Hire Date: {self._hire_date}
            Birth Date: {self._birth_date}
            City: {self._city}
            Street: {self._street}
            Zip Code: {self._zip_code}
            Phone: {self._phone}
        ]"""


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


library1 = Library("Katowice", "ul. Księżycowa 34", "41-615", "7-18", "123456789")
library2 = Library("Zabrze", "ul. Słoneczna 24", "43-230", "8-20", "987654321")

book1 = Book(library1, "1997-06-26", "J.K.", "Rowling", 223)
book2 = Book(library1, "1954-07-29", "J.R.R.", "Tolkien", 423)
book3 = Book(library2, "1949-06-08", "George", "Orwell", 328)
book4 = Book(library2, "1925-04-10", "F. Scott", "Fitzgerald", 218)
book5 = Book(library1, "2001-05-15", "Andrzej", "Sapkowski", 340)

employee1 = Employee("Anna", "Nowak", "2020-01-15", "1990-05-20", "Katowice", "ul. Długa 5", "40-001", "111222333")
employee2 = Employee("Jan", "Kowalski", "2018-03-10", "1985-11-02", "Zabrze", "ul. Krótka 10", "41-800", "444555666")
employee3 = Employee("Piotr", "Zieliński", "2022-07-01", "1995-08-15", "Gliwice", "ul. Jasna 2", "44-100", "777888999")

student1 = Student("Michał Wiśniewski", marks=[55, 45])
student2 = Student("Katarzyna Wójcik", marks=[75, 80])
student3 = Student("Tomasz Lis", marks=[80, 90])

order1 = Order(employee1, student1, [book1, book2, book5], "2023-10-21")
order2 = Order(employee2, student2, [book3, book4], "2023-10-22")

print(order1)
print(order2)
