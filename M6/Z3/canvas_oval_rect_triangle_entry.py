from tkinter import *


def draw_oval():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_oval(100, 100, 200, 200, outline=out_color, fill=color)


def draw_rectangle():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_rectangle(50, 50, 150, 150, outline=out_color, fill=color)


def draw_triangle():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_polygon(50, 150, 100, 50, 150, 150, outline=out_color, fill=color)


def clear_canvas():
    canvas.delete("all")


window = Tk()
window.geometry("400x600")
window.title("Oval Triangle")
canvas = Canvas(window, width=300, height=200)
canvas.pack()

canvas2 = Canvas(window, width=300, height=200, background="white")
canvas2.config(bg="white")

color_var = StringVar(value="blue")
outline_color_var = StringVar(value="red")

oval_button = Button(window, text="Oval", command=draw_oval)
oval_button.pack(pady=10)

triangle_button = Button(window, text="Triangle", command=draw_triangle)
triangle_button.pack(pady=10)

rectangle_button = Button(window, text="Rectangle", command=draw_rectangle)
rectangle_button.pack(pady=10)

clear_button = Button(window, text="Clear", command=clear_canvas)
clear_button.pack(pady=10)

Label(text="Fill color").pack()
color_entry = Entry(window, textvariable=color_var)
color_entry.pack(pady=10)
# color_entry.insert(0, "blue")

Label(text="Outline color").pack()
outline_color_entry = Entry(window, textvariable=outline_color_var)
outline_color_entry.pack(pady=10)
# outline_color_entry.insert(0, "blue")


window.mainloop()
