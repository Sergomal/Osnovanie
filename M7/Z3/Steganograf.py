from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from PIL import Image
import stepic


def open_file():
    file = fd.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg*.bmp")])
    # file = fd.askopenfilename(filetypes=(("Image files", "*.jpg; *.jpeg"), ("All Files", "*.*")))
    file_path.set(file)


def encode_text():
    image_path = file_path.get()
    text = text_to_encode.get()
    output_path = "encoded_image.png"
    try:
        image = Image.open(image_path)
        encoded_image = stepic.encode(image, text.encode())
        encoded_image.save(output_path)
        mb.showinfo("Encoded Image", f"Image saved")  #  at {output_path}
    except Exception as e:
        mb.showerror("Encoded Image Error", str(e))


def decode_text():
    image_path = file_path.get()
    try:
        image = Image.open(image_path)
        decoded_text = stepic.decode(image)
        mb.showinfo("Decoded Text", decoded_text)
    except Exception as e:
        mb.showerror("Decoded Text Error", str(e))


window = Tk()
window.title("Steganograf")
window.geometry("500x500")

file_path = StringVar()
text_to_encode = StringVar()

Label(window, text="Путь к изображению: ").pack()
Entry(window, textvariable=file_path, width=60).pack()
Button(text="Выбрать файл", command=open_file).pack()

Label(window, text="Текст для шифрования: ").pack()
Entry(window, textvariable=text_to_encode, width=60).pack()
Button(text="Зашифровать", command=encode_text).pack()
Button(text="Расшифровать", command=decode_text).pack()


window.mainloop()
