import tkinter as tk
import time
from tkinter import messagebox as mb


def load_phrase():
    try:
        with open("phrase.txt", "r") as f:
            return f.read().strip()

    except FileNotFoundError:
        mb.showerror("Error", "fnf")
        return "fox"  # quickbrownfox


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


def cont(event):  # def cont(event)
    global i
    label.config(text=phrase[i])
    window.bind("<Key>", check)


i = 0
t = None
phrase = load_phrase()


window = tk.Tk()
window.title("Клавиатурный тренажер")
window.geometry("900x100")

label = tk.Label(window, font=("Helvetica", 24))
label.pack()


start()

window.mainloop()
