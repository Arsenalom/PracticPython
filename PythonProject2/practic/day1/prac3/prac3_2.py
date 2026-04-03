import random

def check(x):
    y = int(input("Введи число: "))

    if x == y:
        print("Умничка!")
    elif x < y:
        print("Загаданное число меньше")
        check(x)
    else:
        print("Загаданное число больше")
        check(x)

print("Угадай 1 до 10")
check(random.randint(1, 10))
