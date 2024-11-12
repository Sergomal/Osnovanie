from tkinter import *


def draw_oval():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_oval(100, 100, 200, 200, outline=out_color, fill=color)


def draw_triangle():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_polygon(250, 200, 300, 100, 350, 200, outline=out_color, fill=color)


def draw_rectangle():
    color = color_entry.get()
    out_color = outline_color_entry.get()
    canvas.create_rectangle(400, 100, 600, 200, outline=out_color, fill=color)


def clear_canvas():
    canvas.delete("all")
    canvas.configure(background="white")


def set_background():
    color = background_color_entry.get()
    canvas.configure(background=color)


window = Tk()
window.geometry("800x600")
window.title("Drawing shapes")

color_var = StringVar(value="red")
outline_color_var = StringVar(value="black")
background_color_var = StringVar(value="white")

canvas = Canvas(window, width=780, height=460, background=background_color_var.get())
canvas.pack(pady=10, padx=10)

bg_frame = Frame(window)
bg_frame.pack()

color_frame = Frame(window)
color_frame.pack()

shape_frame = Frame(window)
shape_frame.pack()

Label(bg_frame, text="Background color:").pack(side=LEFT)
background_color_entry = Entry(bg_frame, textvariable=background_color_var)
background_color_entry.pack(side=LEFT, padx=5, pady=5)

background_button = Button(
    bg_frame, text="Set background", command=set_background, width=11
)
background_button.pack(side=LEFT, padx=5, pady=5)

Label(color_frame, text="Fill color:").pack(side=LEFT, padx=5, pady=5)
color_entry = Entry(color_frame, textvariable=color_var)
color_entry.pack(side=LEFT, padx=5, pady=5)

Label(color_frame, text="Outline color:").pack(side=LEFT, padx=5, pady=5)
outline_color_entry = Entry(color_frame, textvariable=outline_color_var)
outline_color_entry.pack(side=LEFT, padx=5, pady=5)

oval_button = Button(shape_frame, text="Oval", command=draw_oval, width=11)
oval_button.pack(side=LEFT, padx=10, pady=5)

triangle_button = Button(shape_frame, text="Triangle", command=draw_triangle, width=11)
triangle_button.pack(side=LEFT, padx=10, pady=5)

rectangle_button = Button(
    shape_frame, text="Rectangle", command=draw_rectangle, width=11
)
rectangle_button.pack(side=LEFT, padx=10, pady=5)

clear_button = Button(shape_frame, text="Clear", command=clear_canvas, width=11)
clear_button.pack(side=LEFT, padx=10, pady=5)

window.mainloop()
