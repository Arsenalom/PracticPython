x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))

if (x + y > z) and (x + z > y) and (y + z > x):

    if x == y == z:
        print("равносторонний треугольник")
    elif x == y or y == z or x == z:
        print("Равнобедреннй")

    side = sorted([x,y,z])
    if round(side[0]**2 + side[1]**2, 3) ==round(side[2]**2,3):
        print("прямоугольный треугольник")
    if not (x == y or y == z or x == z):
        print("Это разносторонний треугольник")

else:
    print("Треугольник не существует")