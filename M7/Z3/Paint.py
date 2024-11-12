from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image  # +++

canvas_width = 700
canvas_height = 500
brush_size = 3
color = "black"


def save():
    fn = filedialog.asksaveasfilename(
        initialfile="Untitled.png",
        filetypes=[("PNG", ".png"), ("JPG", ".jpg")],
        initialdir="Computer/Images",
    )
    if fn == "":
        return


# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def make_square(im, min_size=256, fill_color=(112, 112, 112)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new("RGBA", (size, size), (255, 255, 255, 255))
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


def load():
    global canvas_obj, tkimage, selectedImage
    #    fl = filedialog.askopenfile(filetypes=[("PNG", ".png"), ("JPG", ".jpg")])
    # ??? TclError: image "<_io.TextIOWrapper name='D:/_Qt/__Qt/lena.jpg' mode='r' encoding='cp1251'>"
    #  doesn't exi
    #    w.create_image(canvas_width, canvas_height, image=fl, anchor=NW)

    pathToImage = filedialog.askopenfilename(
        filetypes=[
            ("PNG Files", "*.png"),
            ("JPG Files", "*.jpg"),
            ("JPEG Files", "*.jpeg"),
        ]
    )

    if not pathToImage:
        return

    image = Image.open(str(pathToImage))
    w, h = image.size
    if w > 650:
        k = w / 650
        _w = int(w / k)
        _h = int(h / k)
        image = image.resize((_w, _h), Image.ANTIALIAS)
    w, h = image.size
    if h > 450:
        k = h / 450
        _w = int(w / k)
        _h = int(h / k)
        image = image.resize((_w, _h), Image.ANTIALIAS)
    tkimage = image

    image = make_square(im=image)
    w, h = image.size
    if w > 700:
        k = w / 700
        _w = int(w / k)
        _h = int(h / k)
        image = image.resize((_w, _h), Image.ANTIALIAS)
    w, h = image.size
    if h > 500:
        k = h / 500
        _w = int(w / k)
        _h = int(h / k)
        image = image.resize((_w, _h), Image.ANTIALIAS)
    w, h = image.size

    selectedImage = ImageTk.PhotoImage(image=image)
    canvas.delete(canvas_obj)
    canvas_obj = canvas.create_image(
        (700 - w) // 2, (500 - h) // 2, anchor=NW, image=selectedImage
    )


# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def brush_size_change(new_size):
    global brush_size
    brush_size = new_size


def color_change(new_color):
    global color
    color = new_color


# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def draw(filename, number_cycles=0):
    global canvas_obj, update, tkimage
    image = Image.open(filename)
    angle = 0
    i = 0
    flag = True
    while flag:
        i += 1
        if i < number_cycles:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = canvas.create_image(350, 250, image=tkimage)
            root.after_idle(update)
            yield
            if i < number_cycles - 1:
                canvas.delete(canvas_obj)
            angle += 10
            angle %= 360
        else:
            yield
            flag = False


# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

root = Tk()
root.title("Paint")

# vvvvv <---- canvas # !!!
# w = Canvas(root, width=canvas_width,
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.bind("<B1-Motion>", paint)

col = Label(root, text="Цвет кисти")
col.grid(row=0, column=0)

size = Label(root, text="Размер кисти")
size.grid(row=8, column=0)

save_btn = Button(text="Сохранить", width=8, command=lambda: save())
load_btn = Button(text="Загрузить", width=8, command=lambda: load())
ten_btn = Button(text="Размер 10", width=8, command=lambda: brush_size_change(10))
five_btn = Button(text="Размер 5", width=8, command=lambda: brush_size_change(5))
two_btn = Button(text="Размер 3", width=8, command=lambda: brush_size_change(3))
fiveten_btn = Button(text="Размер 15", width=8, command=lambda: brush_size_change(15))

yellow_btn = Button(text="Жёлтый", width=10, command=lambda: color_change("yellow"))
brown_btn = Button(text="Коричневый", width=10, command=lambda: color_change("brown"))
black_btn = Button(text="Черный", width=10, command=lambda: color_change("black"))
red_btn = Button(text="Красный", width=10, command=lambda: color_change("red"))
green_btn = Button(text="Зеленый", width=10, command=lambda: color_change("green"))
white_btn = Button(text="Ластик", width=10, command=lambda: color_change("white"))
clear_btn = Button(text="Удалить всё", width=10, command=lambda: canvas.delete("all"))


canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
# +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
canvas_obj = None
selectedImage = None
filename = "lena.jpg"  # можете установить свое изображение
tkimage = Image.open(filename)
update = draw(filename, number_cycles=38).__next__
root.after(500, update)
# +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

canvas.columnconfigure(6, weight=1)
canvas.rowconfigure(2, weight=1)

save_btn.grid(row=8, column=5)
two_btn.grid(row=8, column=1)
five_btn.grid(row=8, column=2)
ten_btn.grid(row=8, column=3)
fiveten_btn.grid(row=8, column=4)

yellow_btn.grid(row=0, column=7)
brown_btn.grid(row=0, column=6)
clear_btn.grid(row=0, column=5)
white_btn.grid(row=0, column=4)
green_btn.grid(row=0, column=3)
black_btn.grid(row=0, column=2)
red_btn.grid(row=0, column=1)

# load()
root.after(2000, load)  # +++

root.mainloop()
