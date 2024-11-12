from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def delete():
    text.delete(1.0, END)


def insert():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, "r", encoding="utf-8") as f:
                s = f.read()
        text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Файл не найден")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")


def save():
    try:
        file = fd.asksaveasfilename(
            filetypes=(
                ("txt file", "*.txt"),
                ("HTML file", "*.html"),
                ("All files", "*.*"),
            )
        )
        if file:
            with open(file, "w", encoding="utf-8") as f:
                s = text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Не удалось сохранить файл")
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка {e}")


window = Tk()

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть", command=insert)
filemenu.add_command(label="Новый", command=delete)
filemenu.add_command(label="Сохранить", command=save)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=quit)
mainmenu.add_cascade(label="Файл", menu=filemenu)

text = Text(width=30, height=8, bg="lightgray", wrap=WORD)
text.pack(side=LEFT)
scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)


text = Text(width=30, height=8, bg="gray", wrap=WORD)
text.pack(side=LEFT)


scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)
b1 = Button(text="Вставка текста", command=insert)
b1.pack(side=LEFT)
b2 = Button(text="Удаление текста", command=delete)
b2.pack(side=LEFT)

b3 = Button(text="Сохранение текста", command=save)
b3.pack(side=LEFT)
window.mainloop()
