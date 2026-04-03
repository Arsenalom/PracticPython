x = int(input("Введите целое число: "))

x = x % 86400

hours = x // 3600
min = (x // 3600) // 60
sec = x % 60

print(f"{hours}:{min}:{sec}")