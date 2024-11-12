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
    check_number(multiple_1, 1)

    multiple_2 = e2.get()
    check_number(multiple_2, 2)

    multiple_3 = e3.get()
    check_number(multiple_3, 3)

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
window.config()  # padx=50, pady=50
frame1 = Frame(window)
frame2 = Frame(window)
frame3 = Frame(window)
frame1.pack(side=LEFT)
frame2.pack(side=LEFT)
frame3.pack(side=BOTTOM)


m = Label(frame1, text="Введите три числа и нажмите на кнопку для вычисления ")
m.pack(anchor=NW)
b_add = Button(frame1, text="суммы тёх чисел", command=summ)
b_add.pack(anchor=NE)
b_mult = Button(frame1, text="произведения трёх чисел", command=multiply)
b_mult.pack(anchor=E)


e1 = Entry(frame2)
e2 = Entry(frame2)
e3 = Entry(frame2)  # Добавление третьего поля для ввода

e1.pack()
e2.pack()
e3.pack()

m1 = Label(frame2)  # height=3
m1.pack(anchor=NW)

main_menu = Menu(window)
window.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=window.destroy)

operation_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Operation", menu=operation_menu)
operation_menu.add_command(label="Addition", command=summ)
operation_menu.add_command(
    label="Multiplication", command=multiply
)  #  command=window.destroy

window.mainloop()
