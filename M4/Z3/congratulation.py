import random


def congratulation(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            con = file.readlines()

        if not con:
            print("Файл пуст.")
        else:
            print(random.choice(con))

    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


congratulation('congrats.txt')
