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


def quit():
    window.destroy()


def update_status():
    content = text.get("1.0", END)
    char_count = len(content)
    word_count = len(content.split())
    status_label.config(text=f"Символов: {char_count} | Слов: {word_count} |")


window = Tk()

frame = Frame(window)
frame.pack()

status_label = Label(window, text="proba", anchor=W)
status_label.pack(fill=X)


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=insert)
file_menu.add_command(label="Сохранить", command=save)
file_menu.add_command(label="Удалить", command=delete)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)


text = Text(frame, width=30, height=8, bg="lightgray", wrap=WORD)
text.pack(side=LEFT)
text.bind("<Key>", lambda event: update_status())
scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)


update_status()

# b1 = Button(text="Вставка текста", command=insert)
# b1.pack(side=LEFT)
# b2 = Button(text="Удаление текста", command=delete)
# b2.pack(side=LEFT)
#
# b3 = Button(text="Сохранение текста", command=save)
# b3.pack(side=LEFT)
window.mainloop()
