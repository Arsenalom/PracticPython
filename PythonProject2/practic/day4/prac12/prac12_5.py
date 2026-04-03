file_name = input("Введите имя файла: ")

try:
    with open(file_name, 'r') as f:
        for line in f:
            # Разбиваем строку на части, превращаем в числа и считаем сумму
            str = sum(int(num) for num in line.split() if num.isdigit())
            print(f"Сумма строки: {str}")
except Exception as e:
    print(f"Ошибка: {e}")
