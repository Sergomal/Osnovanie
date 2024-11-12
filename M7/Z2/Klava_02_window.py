import tkinter as tk
import time
from tkinter import messagebox as mb


def start():
    global i, t
    i = 0
    t = time.time()
    label.config(text=phrase[i])
    window.bind("<Key>", check)


def check(event):
    global i, t
    if event.char == phrase[i]:
        i += 1
        if i == len(phrase):
            finish()
        else:
            label.config(text=phrase[i])
    else:
        label.config(
            text=f"Ошибка! Ожидалась буква '{phrase[i]}',\n нажмите любую клавишу для продолжения"
        )
        window.bind("<Key>", cont)


def finish():
    elapsed = time.time() - t
    time_allowed = len(phrase)
    if elapsed <= time_allowed:
        res = f"Победа! Ваше время: {elapsed:.1f} сек."
        window.unbind("<Key>")
    else:
        res = f"Прошло: {elapsed:.1f} сек. Это много!"
        window.unbind("<Key>")
    mb.showinfo("Result", res)
    if mb.askokcancel("Repeat", "Do you want to repeat?"):
        start()
    else:
        window.destroy()


def cont(event):
    global i
    label.config(text=phrase[i])
    window.bind("<Key>", check)


phrase = "quickbrownfox"


window = tk.Tk()
window.title("Клавиатурный тренажер")
window.geometry("900x100")

label = tk.Label(window, font=("Helvetica", 24))  # text=phrase[i],
label.pack()
# window.bind("<Key>", check)

start()

window.mainloop()
