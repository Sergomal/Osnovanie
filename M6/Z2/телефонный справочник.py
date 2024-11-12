from tkinter import *
from tkinter import messagebox as mb


def add_item():
    # print(s.get())
    if entry.get():
        if var_rb.get() == 1:
            list_names.insert(END, entry.get())
            entry.delete(0, END)
        else:
            if validate_num():
                list_phones.insert(END, entry.get())
                entry.delete(0, END)


def del_name():
    list_names.delete(ANCHOR)


def del_num():
    list_phones.delete(ANCHOR)


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
                f.write(f"{list_names.get(i)}:{list_phones.get(i)}\n")
        mb.showinfo("Сохранение", "Контакты успешно сохранены")
    except Exception as err:
        mb.showerror("Ошибка", f"Ошибка {err}")


window = Tk()
window.title("Телефонный справочник")

var_rb = IntVar(value=1)

# создаем фрейм 1 и размещаем внутри виджеты
frame_names = Frame()
frame_names.pack(side=LEFT)

label_names = Label(frame_names, text="Имена")
label_names.pack()

list_names = Listbox(frame_names)
list_names.pack(side=LEFT)


# создаем фрейм 2 и размещаем внутри виджеты

frame_phones = Frame()
frame_phones.pack(side=LEFT)

label_phones = Label(frame_phones, text="Телефоны")
label_phones.pack()

list_phones = Listbox(frame_phones)
list_phones.pack()


# создаем фрейм 3 и размещаем внутри виджеты

frame_management = Frame()
frame_management.pack(side=LEFT)

rb_name = Radiobutton(frame_management, text="Имя", variable=var_rb, value=1)
rb_name.pack()

r2 = Radiobutton(frame_management, text="Номер", variable=var_rb, value=2)
r2.pack()

entry = Entry(frame_management)
entry.pack()

button_add_item = Button(frame_management, text="Добавить", command=add_item)
button_add_item.pack()

button_del_name = Button(frame_management, text="Удалить имя", command=del_name)
button_del_name.pack()

button_del_num = Button(frame_management, text="Удалить номер", command=del_num)
button_del_num.pack()

button_download = Button(frame_management, text="Загрузка", command=download)
button_download.pack()

button_save = Button(frame_management, text="Сохранить", command=save)
button_save.pack()


window.mainloop()
