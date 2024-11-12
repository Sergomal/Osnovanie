from tkinter import *
import time


import threading  # Импортируем модель для дополнительных процессов
import tkinter as tk
from time import sleep
from datetime import timedelta, datetime

win = tk.Tk()  # создаем окно
win.title("Clock")
time = (datetime.now() + timedelta(hours=5)).strftime("%H:%M:%S")
lbl_time = tk.Label(text=time, font="Verdana 24 bold")  # заранее создаем надпись
lbl_time.pack()  # размещаем ее


def clock_update():  # создаем функцию
    while True:
        # Постоянно меняем значение у наших часов
        lbl_time["text"] = (datetime.now() + timedelta(hours=0)).strftime("%H:%M:%S")
        sleep(
            0.5
        )  # засыпаем на половину секунды, чтобы не перегружать процесс постоянными обновлениями


process = threading.Thread(
    target=clock_update
)  # Создаем процесс, в котором будем обновлять наши часы
process.start()  # Запускаем процесс

win.mainloop()  # Активируем окно


# def tick():
#     t = time.strftime("%H:%M:%S")
#     m.config(text=t)
#     m.after(1000, tick)  # вызовы идут каждую секунду
#
#
# window = Tk()
# m = Label(font="Verdana 24 bold")
# m.pack()
# tick()
# window.mainloop()
