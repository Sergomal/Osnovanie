from tkinter import *
from tkinter import messagebox as mb

"""
Multiply and add
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
    m1["text"] = f"{s1} + {s2} + {s3} = {str(summa)}"

    answer = mb.askretrycancel(title="Вопрос", message="Сложить еще три числа?")
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

    multiple_1 = int(multiple_1)
    multiple_2 = int(multiple_2)
    multiple_3 = int(multiple_3)
    composition = multiple_1 * multiple_2 * multiple_3
    m1["text"] = f"{multiple_1} x {multiple_2} x {multiple_3} = {str(composition)}"

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
window.geometry("500x200")
window.title("Multiply and add")
window.config()

m = Label(window, text="Введите три числа и нажмите на кнопку для вычисления ")
m.pack()
e1 = Entry(width=30)
e2 = Entry(width=30)
e3 = Entry(width=30)

e1.pack()
e2.pack()
e3.pack()

b_add = Button(window, text="суммы тёх чисел", width=25, command=summ)
b_add.pack()

b_mult = Button(window, text="произведения трёх чисел", width=25, command=multiply)
b_mult.pack()

m1 = Label()
m1.pack()

window.mainloop()
