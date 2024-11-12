"""
Доработайте программу калькулятора.
Добавьте функцию, которая позволит пользователю просматривать историю всех выполненных ранее вычислений.
Эта функция будет читать данные из файла, в который записываются результаты (calculations.txt),
и выводить их пользователю.
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Ошибка. Деление на ноль"


def get_number(prompt):
    while True:
        value = input(prompt)
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print("Это не целое число. Пожалуйста, введите целое число.")


def log(result_calculations):
    try:
        with open("calculations.txt", "a", encoding="utf-8") as file:
            file.write(result_calculations + "\n")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def show_history():
    try:
        with open("calculations.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Произошла ошибка {e}")
    else:
        for line in lines:
            print(line, end="")


print("""Выберите операцию:
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Просмотр истории вычислений""")

valid_choices = ['1', '2', '3', '4', '5']
choice = None

while choice not in valid_choices:
    choice = input("Введите номер операции (1/2/3/4/5): ")
    if choice not in valid_choices:
        print("Неверный ввод. Пожалуйста, выберите 1, 2, 3, 4 или 5.")

if choice == '5':
    show_history()
else:
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")

    r = ""

    if choice == '1':
        r = f"Результат: {num1} + {num2} = {add(num1, num2)}"
    elif choice == '2':
        r = f"Результат: {num1} - {num2} = {subtract(num1, num2)}"
    elif choice == '3':
        r = f"Результат: {num1} * {num2} = {multiply(num1, num2)}"
    elif choice == '4':
        r = divide(num1, num2)
        if isinstance(r, str):
            pass
        else:
            r = f"Результат: {num1} / {num2} = {r:.4f}"
    else:
        print("Неверный ввод")

    print(r)
    log(r)
