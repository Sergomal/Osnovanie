from tkinter import *


def show():
    c["fg"] = v.get()
    m["text"] = v.get()


window = Tk()

v = StringVar()
v.set("black")
c = Checkbutton(
    text="Это переключатель цвета",
    variable=v,
    onvalue="magenta",
    offvalue="red",
    command=show,
)
c.pack()

m = Label(text="Label", width=15, height=3, bg="lightgray")
m.pack()
window.mainloop()
