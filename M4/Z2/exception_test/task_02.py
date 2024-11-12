"""
Ломать — не строить

Давайте немного поиграем в «багоюзеров».

Вашему решению будет предоставлена функция func, которая принимает два позиционных параметра
и производит с ними некую математическую операцию.

Предложите вызов функции, который гарантированно породит ошибку внутри функции.
Примечание

Если ошибка произойдёт внутри функции, то она будет перехвачена и обработана.
Если же она произойдет в вашем коде, то программа будет завершена с ошибкой.
Пример 1
Ввод

def func(a, b):
    return a + b

Вывод

Ура! Ошибка!

Пример 2
Ввод

def func(a, b):
    return a * b

Вывод

Ура! Ошибка!
"""


def func(a, b):
    return a * b


q = type("q")
w = type((4, 0))
func(q, w)
