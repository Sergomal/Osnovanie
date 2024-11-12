contacts = {}


def input_contact():
    name = input("Введите имя: ")
    phone = input("Введите телефон (10 цифр, начинающийся с 9): ")
    if len(phone) == 10 and phone.isdigit() and phone.startswith('9'):
        contacts[name] = phone
        print("Контакт успешно добавлен.")
    else:
        print("Ошибка: Неверный формат номера телефона.\
              Номер должен быть 10-значным и начинаться с 9.")


def find_contact():
    name = input("Введите имя для поиска: ")
    print(contacts.get(name, "Контакт не найден"))


def delete_contact():
    name = input("Введите имя для удаления: ")
    if name in contacts:
        del contacts[name]
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")


while True:
    action = input("Выберите действие:\nдобавить\t(1)\nнайти\t\t(2)\nудалить\t\t(3)\nвыйти\t\t(4): ")
    if action == '1':
        input_contact()
    elif action == '2':
        find_contact()
    elif action == '3':
        delete_contact()
    elif action == '4':
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите действие 1, 2, 3 или 4.")
