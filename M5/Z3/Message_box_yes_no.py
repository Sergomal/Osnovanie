from tkinter import *
from tkinter import messagebox as mb


def check():
    #    answer=mb.askyesno(title="Вопрос", message="Перенести данные?")
    #    answer=mb.askretrycancel(title="Вопрос", message="Перенести данные?")
    answer = mb.askokcancel(title="Вопрос", message="Перенести данные?")

    if answer:
        s = e.get()
        e.delete(0, END)
        l.config(text=s)


window = Tk()

e = Entry()
e.pack()

b = Button(text="Передать", command=check)
b.pack()

l = Label()
l.pack()

window.mainloop()
