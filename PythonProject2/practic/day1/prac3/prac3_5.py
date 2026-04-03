def calculate_function():

    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    x1 = float(input("Введите x1: "))
    x2 = float(input("Введите x2: "))
    n = int(input("Введите количество точек N: "))

    if n < 2:
        print("N как минимум 2 (для x1 и x2)")
        return

    step = (x2 - x1) / (n - 1)

    for i in range(n):
        x = x1 + i * step if i < n - 1 else x2

        y = a * x + b

        print(f"y({x:.3f}) = {a}*{x:.3f}+{b} = {y:.3f}")

calculate_function()