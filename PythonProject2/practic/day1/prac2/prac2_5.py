x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
operation =input("Введите операцию(&,|,^,<<,>>): ")

if operation == "&":
    result = x & y
elif operation == "|":
    result = x | y
elif operation == "^":
    result = x ^ y
elif operation == "<<":
    result = x << y
elif operation == ">>":
    result = x >> y
else:
    result = None
    print("Неверная операция")

if result is not None:
    print(f"\nЧисло A:  {x:b} ({x})")
    print(f"Число B:  {y:b} ({y})")
    print(f"Результат: {result:b} ({result})")