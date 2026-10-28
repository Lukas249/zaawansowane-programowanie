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
