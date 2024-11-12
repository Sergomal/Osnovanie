from tkinter import *
import datetime as dt


def datetime():
    m.config(text=f"{Date} {Time}")


def date():
    m.config(text=Date)


def time():
    m.config(text=Time)


def night():
    m.config(bg="black", fg="white")
    R1.config(bg="black", fg="white")
    R2.config(bg="black", fg="white")
    R3.config(bg="black", fg="white")
    R4.config(bg="black", fg="white")


window = Tk()

d = dt.datetime.now()
Date = d.strftime("%d %B %Y")
print(Date)
Time = d.strftime("%X")
print(Time)

var = IntVar()
var.set(0)

R1 = Radiobutton(text="Дата и время", command=datetime, variable=var, value=0)
R1.pack(side=LEFT)
R2 = Radiobutton(text="Дата", command=date, variable=var, value=1)
R2.pack(side=LEFT)
R3 = Radiobutton(text="Время", command=time, variable=var, value=2)
R3.pack(side=LEFT)
R4 = Radiobutton(text="Ночная тема", command=night, variable=var, value=3)
R4.pack(side=LEFT)


m = Label(font="Verdana 24 bold")
m.pack(side=LEFT)
m.config(text=f"{Date} {Time}")
window.mainloop()
