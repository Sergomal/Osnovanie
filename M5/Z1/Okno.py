from tkinter import *


def change():
    label['text'] = 'чёрная метка'
    label['bg'] = 'black'


window = Tk()
window.geometry('500x500')
window.title('Okno')

label = Label(window, text='Hello World', bg='DarkRed', fg='LightCoral', width=15, height=5)
label.pack()

button = Button(text='Изменить кнопку', width=15, height=3)
button.config(command=change)
button.pack()
window.mainloop()
