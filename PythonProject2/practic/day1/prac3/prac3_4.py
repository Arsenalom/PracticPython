def sum():
    price = int(input("Запрашиваемая сумма: "))
    if price <= 0:
        print("повтори")
        return sum()

    payment = int(input("внесено покупателем: "))

    if payment < price:
        diff = price - payment
        print(f"Внесенная сумма меньше запрашиваемой. Требуется доплатить: {diff}")
        return sum()

    if payment == price:
        print("СИПАСИБА")
    else:
        change = payment - price
        print(f"Сдача: {change}")
        print("СИПАСИБА")

sum()
