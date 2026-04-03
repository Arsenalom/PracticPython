import random

x = random.randint(1,100)

division = 0
for i in range(1, x + 1):
    if x % i == 0:
        division += 1

prime = "простое" if division == 2 else "не простое"

print(x)
print(prime)

