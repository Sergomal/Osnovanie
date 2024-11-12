from datetime import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import shutil


def choice_dir():
    directory = fd.askdirectory(title="Выберите папку для копирования")
    if directory:
        organize_photos(directory)


def organize_photos(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif")):
            file_path = os.path.join(directory, filename)
            timeStamp = os.path.getmtime(file_path)
            date = datetime.fromtimestamp(timeStamp)
            year_month = date.strftime("%Y_%m")
            new_dir = os.path.join(directory, year_month)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            shutil.move(file_path, os.path.join(new_dir, filename))
    mb.showinfo("Готово", "Все фото рассортированы")


window = Tk()
window.withdraw()


choice_dir()


window.mainloop()
