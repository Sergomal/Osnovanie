from datetime import datetime
from tkinter import *
from tkinter import filedialog as fd
import os
import shutil


window = Tk()
window.withdraw()

directory = fd.askdirectory(title="Выберите папку для копирования")
if directory:
    new_directory = directory + "_new"
    if not os.path.exists(new_directory):
        try:
            os.makedirs(new_directory)
            # shutil.copytree(directory, new_directory)
            # print(f"Всё содержимое папки {directory} скопировано в {new_directory}.")
        except Exception as e:
            print(str(e))
    else:
        print(f"Папка {new_directory} уже существует")

    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif")):
            source_file = os.path.join(directory, filename)
            destination = os.path.join(new_directory, filename)
            try:
                shutil.move(source_file, destination)
                print("Файл перемещён")
            except Exception as e:
                print(f"Ошибка перемещения файла {filename}:{e}")

    print("Всё скопировано")
else:
    print(f"Папка не была выбрана")


window.mainloop()
