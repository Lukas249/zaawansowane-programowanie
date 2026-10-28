def flatten_list(nested_list: list) -> list:

    values = []

    for x in nested_list:
        if type(x) is list:
            values += flatten_list(x)
        else:
            values.append(x)

    return values
