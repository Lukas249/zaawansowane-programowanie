def fn(arr: list, num: int) -> bool:
    return num in arr

print(fn([1, 2, 3, 4, 5], 3))
print(fn([1, 2, 4, 5], 3))