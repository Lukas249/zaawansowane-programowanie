import csv


def load_file(file_name: str) -> list[list]:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        return list(reader)[1:]
