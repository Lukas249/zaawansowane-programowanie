def fibonacci(n):
    if n < 0:
        return None

    num1 = 0
    num2 = 1

    while n > 0:
        num1, num2 = num2, num1 + num2
        n -= 1

    return num1
