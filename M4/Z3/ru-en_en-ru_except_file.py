"""
dict = {
    "кошка": "cat",
    "собака": "dog",
    "лошадь": "horse",
    "утка": "duck",
    "птица": "bird",
    "слон": "elephant",
    "cat": "кошка",
    "dog": "собака",
    "horse": "лошадь",
    "duck": "утка",
    "bird": "птица",
    "elephant": "слон",

}
"""


def save_dictionary_to_file(dict_to_save):
    try:
        with open('dictionary.txt', 'w', encoding="utf-8") as file:
            for key, value in dict_to_save.items():
                file.write(f"{key}:{value}\n")
                print(f"{key}:{value} add to dictionary.txt")
                file.flush()
    except Exception as e:
        print(e)
    else:
        print(f"словарь успешно сохранён в файл: OK")


def load_dictionary_from_file(filename):
    dictionary = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                key, value = line.rstrip().split(":")
                dictionary[key] = value
    except FileNotFoundError:
        print("Файл словаря не найден.")
    except ValueError:
        print("Ошибка в формате словаря.")
    return dictionary


dict_RAM = load_dictionary_from_file("dictionary.txt")

word = None
while word != "q":
    print("Для выхода введите 'q'")
    word = input("Введите слово: ").lower()
    if word == "q" or word == "й":
        save_dictionary_to_file(dict_RAM)
        break
    try:
        print(f"Перевод: {word} = {dict_RAM[word]}")
    except KeyError:
        print(dict_RAM.get(word, "Нет такого слова. Добавляем в словарь..."))
        new_tr = input(f"Введите перевод слова {word}: ")
        dict_RAM[word] = new_tr
        print(f"Словарная пара {word} = {new_tr} добавлена в словарь.")
        dict_RAM[new_tr] = word
        print(f"Словарная пара {new_tr} = {word} добавлена в словарь.")
