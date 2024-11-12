from tkinter import *
from tkinter import messagebox as mb


def add_item():
    if entry.get():
        if var_rb.get() == 1:
            list_names.insert(END, entry.get())
            entry.delete(0, END)
        else:
            if validate_num():
                list_phones.insert(END, entry.get() + "\n")
                entry.delete(0, END)


def del_contact():
    index = list_names.curselection()
    print(index[0])
    list_names.delete(ANCHOR)
    list_phones.delete(index[0])


def del_name():
    index = list_names.curselection()
    print(index[0])
    list_names.delete(ANCHOR)
    list_phones.delete(index[0])


def del_num():
    list_phones.delete(ANCHOR)
    # list_names.delete(ANCHOR)


def download():
    try:
        with open("contacts.txt", "r", encoding="utf-8") as f:
            list_names.delete(0, END)
            list_phones.delete(0, END)
            for line in f:
                name, number = line.split(":")
                list_names.insert(END, name)
                list_phones.insert(END, number)
        mb.showinfo("Успех", "Контакты успешно загружены")
    except FileNotFoundError:
        print("Файл не найден")


def validate_num():
    num = entry.get()
    if len(num) == 10 and num.isdigit() and num.startswith("9"):
        return True
    else:
        mb.showerror("Ошибка", "Проверьте правильность номера")
        entry.delete(0, END)
        return False


def save():
    try:
        with open("contacts.txt", "w", encoding="utf-8") as f:
            for i in range(list_names.size()):  # size находит размер листбокса
                f.write(f"{list_names.get(i)}:{list_phones.get(i)}")
        mb.showinfo("Сохранение", "Контакты успешно сохранены")
    except Exception as err:
        mb.showerror("Ошибка", f"Ошибка {err}")


def yscroll1(*args):
    if list_names.yview() != list_phones.yview():
        list_phones.yview_moveto(args[0])
    scrollbar.set(*args)


def yscroll2(*args):
    if list_names.yview() != list_phones.yview():
        list_names.yview_moveto(args[0])
    scrollbar.set(*args)


def yview(*args):
    list_names.yview(*args)
    list_phones.yview(*args)


window = Tk()
window.title("Телефонный справочник")

var_rb = IntVar(value=1)

frame_lists_names = Frame()
frame_lists_names.pack(side=LEFT)

frame_lists_phones = Frame()
frame_lists_phones.pack(side=LEFT)

frame_management = Frame()
frame_management.pack(side=LEFT)

frame_radio = Frame(frame_management)
frame_radio.pack()

frame_buttons = Frame(frame_management)
frame_buttons.pack()

label_names = Label(frame_lists_names, text="Имена")
label_names.pack()

list_names = Listbox(frame_lists_names, yscrollcommand=yscroll1)
list_names.pack(fill="y", side="left")

label_phones = Label(frame_lists_phones, text="Телефоны")
label_phones.pack()

list_phones = Listbox(frame_lists_phones, yscrollcommand=yscroll2)
list_phones.pack(expand=1, fill="both", side="left")

scrollbar = Scrollbar(frame_lists_phones, orient="vertical")
scrollbar.config(command=yview)
scrollbar.pack(side="right", fill="y")


rb_name = Radiobutton(frame_radio, text="Имя", variable=var_rb, value=1)
rb_name.pack(side="left")

r2 = Radiobutton(frame_radio, text="Номер", variable=var_rb, value=2)
r2.pack(side="left")

entry = Entry(frame_buttons, width=24)
entry.pack()

button_add_item = Button(frame_buttons, text="Добавить", width=20, command=add_item)
button_add_item.pack()

button_del_name = Button(frame_buttons, text="Удалить имя", width=20, command=del_name)
button_del_name.pack()

button_del_num = Button(frame_buttons, text="Удалить номер", width=20, command=del_num)
button_del_num.pack()

button_download = Button(frame_buttons, text="Загрузка", width=20, command=download)
button_download.pack()

button_save = Button(frame_buttons, text="Сохранить", width=20, command=save)
button_save.pack()


window.mainloop()
