from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set_time():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в 24 часовом формате: ЧЧ:ММ")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            # print(now)
            dt = now.replace(hour=hour, minute=minute)
            # print(dt)
            # print(now.timestamp())
            t = dt.timestamp()
            # print(t)
        except Exception as e:
            mb.showerror("Error", f"Error: {e}")
        check()


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = 0
        # print(t - now)
    window.after(10000, check)


def play_snd():
    print("play_snd")
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()


t = 0

window = Tk()
window.geometry("500x500")
window.title("Напоминание")

label = Label(text="Установите напоминание")
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set_time)
set_button.pack()


window.mainloop()
