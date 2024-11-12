s = ["С", "новым", "годом!"]
text = " ".join(s)
print(text)  # Вывод: С новым годом!

s = ["яблоко", "банан", "вишня"]
text = ", ".join(s)
print(text)  # Вывод: яблоко, банан, вишня

s = ["C:", "Python", "Scripts", "Join_1.py"]
text = "\\".join(s)
print(text)

s = ["Царь недолго собирался:",
     "В тот же вечер обвенчался.",
     "Царь Салтан за пир честной",
     "Сел с царицей молодой;"]
text = "\n".join(s)
print(text)

s = [' /\\ /\\ ', '((ovo))', '():::()', '  VVV']
text = "\n".join(s)
print(text)


s = ['    __', '___( o)>', '\\ <_. )', " `---'"]
text = "\n".join(s)
print(text)
