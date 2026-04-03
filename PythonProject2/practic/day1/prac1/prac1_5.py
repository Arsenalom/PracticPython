import math

x = float(input("Введите вещественное число: "))
N = int(input('Введите количество знаков после запятой(N): '))

print("{:.3f}".format(x))
print(f"{round(x, N)}")
