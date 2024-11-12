from tkinter import *
from tkinter import messagebox as mb

"""
Multiply and add
Панель Menu
Подменю File 
        с функцией выхода
Подменю Operation 
        с функцией Addition для сложения трёх чисел
        с функцией Multiplication для умножения трёх чисел
        
Три поля ввода для целых чисел

"""


def check_number(in_num: str, n_fild: int):
    start_message = ""
    if n_fild == 1:
        start_message = "В первое "
    elif n_fild == 2:
        start_message = "Во второе "
    elif n_fild == 3:
        start_message = "В третье "

    if not in_num.lstrip("-").isdigit():
        mb.showerror("Ошибка", start_message + "поле должно быть введено число")
        return True
    return


def summ():
    s1 = e1.get()
    if check_number(s1, 1):
        return

    s2 = e2.get()
    if check_number(s2, 2):
        return

    s3 = e3.get()
    if check_number(s3, 3):
        return

    summa = int(s1) + int(s2) + int(s3)
    m1["text"] = f"{s1} + {s2} + {s3} = {summa}"

    answer = mb.askretrycancel(
        title="Вопрос", message="Хотите выполнить ещё вычисления?"
    )
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1["text"] = ""
    else:
        window.destroy()


def multiply():
    multiple_1 = e1.get()
    if check_number(multiple_1, 1):
        return

    multiple_2 = e2.get()
    if check_number(multiple_2, 2):
        return

    multiple_3 = e3.get()
    if check_number(multiple_3, 3):
        return

    composition = int(multiple_1) * int(multiple_3) * int(multiple_3)
    m1["text"] = f"{multiple_1} x {multiple_2} x {multiple_3} = {composition}"

    answer = mb.askretrycancel(
        title="Вопрос", message="Хотите выполнить ещё вычисления?"
    )
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1["text"] = ""
    else:
        window.destroy()


window = Tk()
window.geometry("500x300")
window.title("Multiply and add")
window.config(padx=50, pady=50)

m = Label(height=3, text="Введите три числа и выберете операцию в меню =Operation=")
m.pack()
e1 = Entry(width=30)
e1.pack()
e2 = Entry(width=30)
e2.pack()
e3 = Entry(width=30)
e3.pack()

m1 = Label()
m1.pack()

main_menu = Menu(window)
window.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.destroy)

operation_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Operation", menu=operation_menu)
operation_menu.add_command(label="Addition", command=summ)
operation_menu.add_command(label="Multiplication", command=multiply)


window.mainloop()
