"""
Задание 3.

Дан код, который выводит список слов, начинающихся на букву “м”


words = ["море", "солнце", "майка", "отпуск"]

a_words = [i for i in words if i.startswith('м')]

print(a_words)


Сделайте программу, которая выводит список слов, оканчивающихся на букву “е”
"""

words = ["море", "солнце", "майка", "отпуск"]

e_words = [i for i in words if i.endswith('е')]

print(e_words)
