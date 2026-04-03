import re


string = input("Введите пароль: ")


if len(string) >=6 and re.search(r'\d',string) and re.search(r'[a-z]',string) and re.search(r'[A-Z]',string):
    print("Пароль сложный")
else:
    print("Пароль лёгкий")