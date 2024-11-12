d = {
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
w = None
while w != "q":
    print("Для выхода введите 'q'")
    w = input("Введите слово: ").lower()
    if w == "q" or w == "й":
        break
    try:
        print(f"Перевод: {w} = {d[w]}")
    except KeyError:
        print(d.get(w, "Нет такого слова. Добавляем в словарь..."))
        new_tr = input(f"Введите перевод слова {w}: ")
        d[w] = new_tr
        print(f"Словарная пара {w} = {new_tr} добавлена в словарь.")
        d[new_tr] = w
        print(f"Словарная пара {new_tr} = {w} добавлена в словарь.")
