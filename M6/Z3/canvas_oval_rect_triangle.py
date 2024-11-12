from tkinter import *


def draw_oval():
    canvas.create_oval(100, 100, 200, 200, outline="red", fill="red")


def draw_rectangle():
    canvas.create_rectangle(50, 50, 150, 150, outline="blue", fill="blue")


def draw_triangle():
    canvas.create_polygon(50, 150, 100, 50, 150, 150, outline="green", fill="green")


def clear_canvas():
    canvas.delete("all")


window = Tk()
window.geometry("400x500")
window.title("Oval Triangle")
canvas = Canvas(window, width=300, height=200)
canvas.pack()

oval_button = Button(window, text="Oval", command=draw_oval)
oval_button.pack(pady=10)

triangle_button = Button(window, text="Triangle", command=draw_triangle)
triangle_button.pack(pady=10)

rectangle_button = Button(window, text="Rectangle", command=draw_rectangle)
rectangle_button.pack(pady=10)

clear_button = Button(window, text="Clear", command=clear_canvas)
clear_button.pack(pady=10)

window.mainloop()
