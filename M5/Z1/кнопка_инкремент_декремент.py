from tkinter import *

a = 0


def change_increment():
    global a
    a += 1
    label['text'] = a


def change_decrement():
    global a
    a -= 1
    label['text'] = a



window = Tk()
window.geometry('500x500')
window.title('Okno')

label = Label(window, text=a, bg='DarkRed', fg='LightCoral', width=15, height=5)
label.pack()

button_increment = Button(text='Инкремент', width=15, height=3)
button_increment.config(command=change_increment)
button_increment.pack()

button_decrement = Button(text='Деремент', width=15, height=3)
button_decrement.config(command=change_decrement)
button_decrement.pack()
window.mainloop()
