def load_file(file_name: str):
    file = open(file_name, "r", encoding="utf-8")

    line = file.readline()

    columns = [line.strip() for line in line.split(",")]

    data = []

    line = file.readline()

    while line:
        row = [line.strip() for line in line.split(",")]

        obj = {}

        for i in range(len(columns)):
            obj[columns[i]] = row[i]

        data.append(obj)

        line = file.readline()

    file.close()

    return data