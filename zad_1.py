from typing import List


class Student:

    def __init__(self, name: str, marks: List[int]) -> None:
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return sum(self._marks) / len(self._marks) > 50

    def __str__(self) -> str:
        return f"""Student[
            name: {self._name},
            marks: {self._marks}   
        ]"""


if __name__ == "__main__":
    student1 = Student("Jan", [100, 0, 45])
    print(student1.is_passed())

    student2 = Student("Marek", [80, 60, 30])
    print(student2.is_passed())