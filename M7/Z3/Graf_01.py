from tkinter import *


pen_color = "black"


# Функция для рисования на холсте
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color)


def change_to_red(event):
    global pen_color
    pen_color = "red"


def change_to_green(event):
    global pen_color
    pen_color = "green"


def change_to_yellow(event):
    global pen_color
    pen_color = "yellow"


window = Tk()
window.title("Рисование на холсте")

canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

red_label = Label(bg="red", width=8, height=2)
red_label.pack(side=LEFT)
red_label.bind("<Button-1>", change_to_red)

green_label = Label(bg="green", width=8, height=2)
green_label.pack(side=LEFT)
green_label.bind("<Button-1>", change_to_green)


yellow_label = Label(bg="yellow", width=8, height=2)
yellow_label.pack(side=LEFT)
yellow_label.bind("<Button-1>", change_to_yellow)


window.mainloop()
