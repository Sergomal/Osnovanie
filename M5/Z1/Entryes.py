from tkinter import *


# a = 128512
#
#
# def smile():
#     # global a
#     return chr(a)
#
#
# def change_increment():
#     global a
#
#     a += 1
#     label['text'] = smile()
#
#
# def change_decrement():
#     global a
#     a -= 1
#     label['text'] = smile()

def read_login():
    login = login_entry.get()
    print(login)
    login_entry.delete(0, END)


def read_pass():
    password = pass_entry.get()
    print(password)
    pass_entry.delete(0, END)


window = Tk()
# window.geometry('500x500')
window.title('Поле ввода')

frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

login_fild = Label(frame_top, text='Login:', width=9, bg='gray', fg='white', font=('Courier', 18, 'bold'))
login_fild.pack(side=LEFT)

login_entry = Entry(frame_top, width=50, justify='center', bg='gray', fg='white', font=('Courier', 18, 'bold'))
login_entry.pack(side=LEFT)

button_Enter_login = Button(frame_top, text='Enter', justify='center', bg='gray', fg='white',
                            font=('Courier', 18, 'bold'))
button_Enter_login.config(command=read_login)
button_Enter_login.pack(side=LEFT)

pass_fild = Label(frame_bottom, text='Password:', bg='gray', fg='white', font=('Courier', 18, 'bold'))
pass_fild.pack(side=LEFT)
pass_entry = Entry(frame_bottom, width=50, justify='center', bg='gray', fg='white', font=('Courier', 18, 'bold'))
pass_entry.pack(side=LEFT)

button_Enter = Button(frame_bottom, text='Enter', justify='center', bg='gray', fg='white', font=('Courier', 18, 'bold'))
button_Enter.config(command=read_pass)
button_Enter.pack(side=LEFT)
window.update()
#
# label_1 = Label(frame_top, text='Metka1', bg='red', fg='LightCoral')  # , font=('Arial', 64)
# label_1.pack(side=LEFT)
# label_2 = Label(frame_top, text='Metka2', bg='yellow', fg='LightCoral')  # , font=('Arial', 64)
# label_2.pack(side=LEFT)
# label_3 = Label(frame_top, text='Metka3', bg='green', fg='LightCoral')  # , font=('Arial', 64)
# label_3.pack(side=LEFT)
# label_4 = Label(frame_bottom, text='Metka4', bg='blue', fg='LightCoral')  # , font=('Arial', 64)
# label_4.pack(side=LEFT)
# label_5 = Label(frame_bottom, text='Metka5', bg='gray', fg='LightCoral')  # , font=('Arial', 64)
# label_5.pack(side=LEFT)
# label_6 = Label(frame_bottom, text='Metka6', bg='brown', fg='LightCoral')  # , font=('Arial', 64)
# label_6.pack(side=LEFT)


# button_decrement = Button(text='PREVIOUS', width=15, height=3)
# button_decrement.config(command=change_decrement)
# button_decrement.pack()
window.mainloop()
