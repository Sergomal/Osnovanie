from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from PIL import Image, ImageTk


def show_thumb():
    img = Image.open("exampl.jpg")
    max_size = (100, 100)
    img.thumbnail(max_size)
    # img = img.resize(max_size)
    img.show()


# show_thumb()
def open():
    try:
        file = fd.askopenfilename()
        if file:
            img = Image.open(file)
            imgconv = img
            width = int(ws.get())
            height = int(hs.get())
            img.thumbnail((width, height))
            imgtk = ImageTk.PhotoImage(img)
            img_window = Toplevel(window)
            img_window.geometry("500x500")
            img_window.title("Image")

            l = Label(img_window, image=imgtk)
            l.pack()

            l.image = imgtk
            # img.show()
    except Exception as e:
        mb.showerror("Error", str(e))


window = Tk()
window.geometry("500x500")
window.title("MyPhoto")

l_width_window = Label(window, text="Width")
l_width_window.pack()

ws = Spinbox(window, from_=100, to=500, increment=100)
ws.pack()


l_height_window = Label(window, text="Height")
l_height_window.pack()

hs = Spinbox(window, from_=100, to=500, increment=100)
hs.pack()


main_menu = Menu(window)
window.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open...", command=open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.destroy)

window.mainloop()
