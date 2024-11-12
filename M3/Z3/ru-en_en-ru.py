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
    w = input("Введите слово: ")
    if w in d:
        print(f"Перевод: {w} = {d[w]}")
    else:
        if w == "q":
            break
        print(d.get(w, "Нет такого слова. Добавляем в словарь..."))
        new_tr = input(f"Введите перевод слова {w}: ")
        d[w] = new_tr
        d[new_tr] = w
