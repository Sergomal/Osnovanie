from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from transliterate import translit, get_available_language_codes
from googletrans import Translator, LANGUAGES


from tkinter.font import Font, families
from tkinter import simpledialog as sd


def delete():
    text.delete(1.0, END)
    update_status()


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
    update_status()


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


def transliter():
    try:
        source_text = text.get(1.0, END)
        t_text = translit(source_text, "ru", reversed=True)
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    update_status()


def translate():
    try:
        source_text = text.get(1.0, END)
        translator = Translator()
        t_text = translator.translate(source_text, src="ru", dest="en").text
        text.delete(1.0, END)
        text.insert(1.0, t_text)
    except Exception as e:
        mb.showerror("Ошибка", f"Ошибка перевода: {e}")


def change_font():
    font_family = sd.askstring("Шрифт", "Введите название шрифта:")
    font_size = sd.askstring("Размер шрифта", "Введите размер шрифта:")
    if font_family and font_size:
        try:
            new_font = Font(family=font_family, size=int(font_size))
            text.configure(font=new_font)
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")


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

process_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Обработка", menu=process_menu)
process_menu.add_command(label="Транслитерация", command=transliter)
process_menu.add_command(label="Перевод ru-en", command=translate)
process_menu.add_separator()
process_menu.add_command(label="Изменить шрифт и размер", command=change_font)


text = Text(frame, width=30, height=8, bg="lightgray", wrap=WORD)
text.pack(side=LEFT)
text.bind("<Key>", lambda event: update_status())
scroll = Scrollbar(frame, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)


update_status()


window.mainloop()
