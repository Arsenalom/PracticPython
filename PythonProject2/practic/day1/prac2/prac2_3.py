year = int(input("Введите год: "))
month = int(input("Введите месяц: "))

x = (year % 4 ==0 and year % 100 != 0) or (year % 400 ==0)

days = (29 if x else 28) if month == 2 else \
    (30 if x in(4,6,9,11) else 31)

print(f"Количество дней в {month} месяце {year} года: {days}")