from tkinter import *
from PIL import Image, ImageTk, ImageGrab
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def set_thickness():
    global thickness
    thickness = int(entry.get())


def draw(event):
    globals()
    x, y = event.x, event.y
    canvas.create_oval(
        x,
        y,
        x + thickness,
        y + thickness,
        fill=pen_color,
        outline=pen_color,
    )


def load_image():
    file_path = fd.askopenfilename(
        filetypes=[("Image Files", "*.png; *.jpg; *.jpeg; *.bmp; *.gif")]
    )
    if file_path:
        try:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
        except Exception as e:
            mb.showerror("Error", str(e))


def save_image():
    try:
        file_path = fd.asksaveasfilename(
            defaultextension=".png", filetypes=[("PNG Files", "*.png;")]
        )
        if file_path:
            x = canvas.winfo_rootx()
            y = canvas.winfo_rooty()
            x1 = x + 600
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Saved Image", file_path)
    except Exception as e:
        mb.showerror("Error", str(e))


pen_color = "black"
thickness = 5

window = Tk()
window.title("Графический редактор")

frame_canvas = Frame(window)
frame_canvas.pack()

canvas = Canvas(frame_canvas, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

frame_color = Frame(window)
frame_color.pack()

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "lightBlue",
    "DeepSkyBlue",
    "blue",
    "violet",
    "purple",
    "brown",
    "black",
]
for color in colors:
    lbl = Label(frame_color, bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

frame_thickness = Frame(window)
frame_thickness.pack()

Label(frame_thickness, text="Толщина линии:").pack(side=LEFT)
entry = Entry(frame_thickness, width=10)
entry.pack(side=LEFT)
Button(frame_thickness, text="Установить толщину", command=set_thickness).pack(
    side=LEFT
)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Download Image", command=load_image)
file_menu.add_command(label="Save Image", command=save_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

window.mainloop()
