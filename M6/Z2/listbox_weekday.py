from tkinter import *

window = Tk()
l = Listbox(width=15, height=7)
l.pack()

"""l.insert(0, "Понедельник")
l.insert(1, "Вторник")
l.insert(2, "Среда")
l.insert(3, "Четверг")
l.insert(4, "Пятница")
l.insert(5, "Суббота")
l.insert(6, "Воскресенье")"""

# заполнение с помощью списка
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
for i in days:
    l.insert(END, i)
window.mainloop()
