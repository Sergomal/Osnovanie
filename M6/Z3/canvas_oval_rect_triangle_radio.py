from tkinter import *


def draw_oval():
    color = color_var.get()
    canvas.create_oval(100, 100, 200, 200, outline=color, fill=color)


def draw_rectangle():
    color = color_var.get()
    canvas.create_rectangle(50, 50, 150, 150, outline=color, fill=color)


def draw_triangle():
    color = color_var.get()
    canvas.create_polygon(50, 150, 100, 50, 150, 150, outline=color, fill=color)


def clear_canvas():
    canvas.delete("all")


window = Tk()
window.geometry("400x600")
window.title("Oval Triangle")
canvas = Canvas(window, width=300, height=200)
canvas.pack()

color_var = StringVar(value="blue")

oval_button = Button(window, text="Oval", command=draw_oval)
oval_button.pack(pady=10)

triangle_button = Button(window, text="Triangle", command=draw_triangle)
triangle_button.pack(pady=10)

rectangle_button = Button(window, text="Rectangle", command=draw_rectangle)
rectangle_button.pack(pady=10)

clear_button = Button(window, text="Clear", command=clear_canvas)
clear_button.pack(pady=10)

blue_radio = Radiobutton(text="Blue", variable=color_var, value="blue")
blue_radio.pack(pady=10)

red_radio = Radiobutton(text="Red", variable=color_var, value="red")
red_radio.pack(pady=10)

green_radio = Radiobutton(text="Green", variable=color_var, value="green")
green_radio.pack(pady=10)

window.mainloop()
