from zad_2.Book import Book
from zad_2.Employee import Employee
from zad_2.Library import Library
from zad_2.Order import Order
from zad_1.Student import Student

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
