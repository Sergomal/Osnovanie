import tkinter as tk
import time


def check(event):
    global i, t
    if event.char == phrase[i]:
        i += 1
        if i == len(phrase):
            elapsed = time.time() - t
            time_allowed = len(phrase)
            if elapsed <= time_allowed:
                label.config(text=f"You WIN!\nYour time {elapsed:.2f} sec.")
                window.unbind("<Key>")
            else:
                label.config(
                    text=f"Sorry!\nYour time {elapsed:.2f} sec.\nIt's more then {time_allowed} sec."
                )
                window.unbind("<Key>")
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
        label.config(text=f"Победа! Ваше время: {elapsed:.1f} сек.")
        window.unbind("<Key>")
    else:
        label.config(text=f"Прошло: {elapsed:.1f} сек. Это много!")


def cont(event):
    global i
    label.config(text=phrase[i])
    window.bind("<Key>", check)


phrase = "quickbrownfox"
i = 0
t = time.time()

window = tk.Tk()
window.title("Клавиатурный тренажер")
window.geometry("900x100")

label = tk.Label(window, text=phrase[i], font=("Helvetica", 24))
label.pack()
window.bind("<Key>", check)

window.mainloop()
