from datetime import datetime
from tkinter import *

n = datetime.now()
print(n)


def set_time():
    pass


def stop_music():
    pass


window = Tk()
window.geometry("500x500")
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set_time)
set_button.pack(pady=10)

stop_button = Button(text="Выключить музыку", command=stop_music)
stop_button.pack(pady=10)


window.mainloop()
