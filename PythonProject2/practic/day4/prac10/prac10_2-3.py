#f7,f8
def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного не определен")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
fact = factorial(num)
print(f"factorial {num} = {fact}")