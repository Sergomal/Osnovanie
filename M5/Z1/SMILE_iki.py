from tkinter import *

a = 128512


def smile():
    # global a
    return chr(a)


def change_increment():
    global a

    a += 1
    label['text'] = smile()


def change_decrement():
    global a
    a -= 1
    label['text'] = smile()


window = Tk()
window.geometry('500x500')
window.title('Okno')

label = Label(window, text=smile(), bg='DarkRed', fg='LightCoral', font=('Arial', 64))
label.pack()

button_increment = Button(text='NEXT', width=15, height=3)
button_increment.config(command=change_increment)
button_increment.pack()

button_decrement = Button(text='PREVIOUS', width=15, height=3)
button_decrement.config(command=change_decrement)
button_decrement.pack()
window.mainloop()
