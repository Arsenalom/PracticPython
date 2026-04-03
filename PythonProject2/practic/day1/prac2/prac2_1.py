import math

x = float(input("Введите x "))

if x < -10:
    y = math.pi * x**2
    print(f"x < -10 : {y:.3f}")

elif -10 <= x < -5:
    print(f"-10 <= x < -5 : {x**4:.3f}")

elif -5 <= x < 10:
    print(f"-5 <= x < 10: {math.e * abs(x):.3f}")

else:
    print(f"x >= 10{1/math.sin(x):.3f}")