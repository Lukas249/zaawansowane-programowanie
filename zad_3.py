def fn(num: int) -> bool:
    return num % 2 == 0


is_even = fn(5)

if is_even:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
