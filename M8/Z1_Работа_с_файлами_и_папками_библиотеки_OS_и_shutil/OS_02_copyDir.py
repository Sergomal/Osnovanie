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
            # os.makedirs(new_directory)
            shutil.copytree(directory, new_directory)
            print(f"Всё содержимое папки {directory} скопировано в {new_directory}.")
        except Exception as e:
            print(str(e))
    else:
        print(f"Папка {new_directory} уже существует")
else:
    print(f"Папка не была выбрана")

    # for filename in os.listdir(directory):
    #     if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif")):
    #         file_path = os.path.join(directory, filename)
    #         lt = os.path.getmtime(file_path)
    #         ft = datetime.fromtimestamp(lt).strftime("%Y-%m-%d %H:%M:%S")
    #
    #         print(filename, ft)


window.mainloop()
