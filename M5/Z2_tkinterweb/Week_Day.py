"""Задание
Запрограммируй чтобы программа выводила день недели на русском языке
в виде фразы “Сегодня понедельник”.
"""

from tkinter import *
import time

window = Tk()
Day = time.strftime("%A")
match Day:
    case "Monday":
        Day = "понедельник"
    case "Tuesday":
        Day = "вторник"
    case "Wednesday":
        Day = "среда"
    case "Thursday":
        Day = "четверг"
    case "Friday":
        Day = "пятница"
    case "Saturday":
        Day = "суббота"
    case "Sunday":
        Day = "воскресенье"
metka = Label(window, font=("Verdana 24 bold"))
metka.pack()
metka.config(text="Сегодня " + Day)
window.mainloop()
