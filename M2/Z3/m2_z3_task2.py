"""
Напишите программу для проверки длины введенного пароля
с использованием цикла while. Программа должна запрашивать
у пользователя ввод пароля и проверять его длину.
Длина пароля должна быть не менее 8 символов.
"""
password_len = 0
while password_len < 8:
    password = input("Введите пароль длинной не менее 8 символов: ")
    password_len = len(password)
    # print(f"Длина пароля {password_len}")
    print("Длина пароля {}".format(password_len))
print("====OK===")