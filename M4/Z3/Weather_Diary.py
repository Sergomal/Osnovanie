def write_to_file(filename, data):
    try:
        with open(filename, 'a', encoding="utf-8") as file:
            file.write(data + "\n")
            print("Данные успешно сохранены.")
    except IOError:
        print("Ошибка при записи файла.")


print("Создатель Дневника Погоды")
while True:
    date = input("Введите дату (или 'выход' для завершения): ")
    if date.lower() == 'выход':
        break
    t = input("Введите температуру: ")
    d = input("Осадки (да/нет): ")

    data = f"{date}: Температура {t}, Осадки {d}"
    write_to_file("weather_diary.txt", data)
