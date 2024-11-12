from datetime import datetime
from tkinter import *
from tkinter import filedialog as fd
import os


window = Tk()
window.withdraw()

directory = fd.askdirectory()
if directory:
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif")):
            file_path = os.path.join(directory, filename)
            lt = os.path.getmtime(file_path)
            ft = datetime.fromtimestamp(lt).strftime("%Y-%m-%d %H:%M:%S")

            print(filename, ft)


window.mainloop()
