x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))

if (x <=y <= z) or (z <=y <= x):
    print(y)
elif (y <= x <= z) or (z <=x <= y):
    print(x)
else:
    print(z)