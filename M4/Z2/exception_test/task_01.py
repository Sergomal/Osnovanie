"""
Обработка ошибок

Вашему решению будет предоставлена функция func, которая не имеет параметров и результата.
Однако во время её исполнения может произойти одна из ошибок: ValueError, TypeError или SystemError.

Вызовите её, обработайте ошибку и выведите её название. Если ошибка не произойдёт,
выведите сообщение "No Exceptions".
Пример 1
Ввод

def func():
    x = int('Hello, world!')

Вывод

ValueError

Пример 2
Ввод

def func():
    x = '2' + 2

Вывод

TypeError

"""


def func():
    # x = int('Hello, world!')
    x = '2' + 2


try:
    func()
except TypeError as e:
    print(e.__class__.__name__)
except ValueError as e:
    print(type(e).__name__)
except SystemError as e:
    print(type(e).__name__)
else:
    print("No Exceptions")
# finally:
#     print("Программа завершена.")
