def fn(a: list, b: list) -> list:
    return [x**3 for x in set(a+b)]


print(fn([1, 2, 3, 4], [5, 6, 7, 8]))
print(fn([1, 2, 3, 4], [3, 4, 7, 8]))
print(fn([1, 2, 3, 4], [1, 2, 3, 4]))
