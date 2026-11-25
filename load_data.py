import csv

def load_file(file_name: str) -> (list, list[list]):
    with open(file_name, "r", encoding="utf-8") as file:

        reader = csv.reader(file, delimiter=",")
        reader_list = list(reader)
        columns = reader_list[0]
        rows = reader_list[1:]
        return columns, rows
