from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


def set_time():
    global t, text
    rem = sd.askstring("Время напоминания", "Введите время в 24 часовом формате: ЧЧ:ММ")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0)
            t = dt.timestamp()
            text = sd.askstring("Текст напоминания", "Введите текст напоминания")
            label.config(text=f"Напоминание на\n{hour:02}:{minute:02}\n{text}")
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
            show_remind()
    window.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()


def show_remind():
    global text
    result = mb.askyesno(
        title="Напоминание со звуковым сигналом",
        message=text,
        detail="Выключить звуковой сигнал?",
    )
    if result:
        stop_music()


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        pygame.quit()
        music = False
    label.config(text="Установить новое напоминание")


t = 0
music = False
text = ""


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
