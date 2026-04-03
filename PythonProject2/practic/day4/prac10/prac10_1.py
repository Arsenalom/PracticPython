def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
print(f"factorial {num} = {factorial((num))}")