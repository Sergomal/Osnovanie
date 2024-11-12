from tkinter import *
from tkinter import messagebox as mb
from random import randint


def check():
    s = int(e.get())
    rnd = randint(1, 2)
    if s == rnd:
        mb.showinfo(title="Угадал!", message=f"Вы угадали, это было число {rnd}")
    else:
        mb.showinfo(title="Не угадал!", message=f"Вы не угадали, это было число {rnd}")

    answer = mb.askretrycancel(title="Вопрос", message="Загадать еще одно число?")
    if answer:
        e.delete(0, END)
    else:
        window.destroy()


window = Tk()
window.title("Угадай число")

l1 = Label(height=3, text="Введите число в поле ввода и нажмите кнопку")
l1.pack()

e = Entry()
e.pack()

b = Button(text="Передать", command=check)
b.pack()

window.mainloop()
