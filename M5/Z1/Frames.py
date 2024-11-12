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


window = Tk()
# window.geometry('500x500')
window.title('Okno')

frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

label_1 = Label(frame_top, text='Metka1', bg='red', fg='LightCoral')  # , font=('Arial', 64)
label_1.pack(side=LEFT)
label_2 = Label(frame_top, text='Metka2', bg='yellow', fg='LightCoral')  # , font=('Arial', 64)
label_2.pack(side=LEFT)
label_3 = Label(frame_top, text='Metka3', bg='green', fg='LightCoral')  # , font=('Arial', 64)
label_3.pack(side=LEFT)
label_4 = Label(frame_bottom, text='Metka4', bg='blue', fg='LightCoral')  # , font=('Arial', 64)
label_4.pack(side=LEFT)
label_5 = Label(frame_bottom, text='Metka5', bg='gray', fg='LightCoral')  # , font=('Arial', 64)
label_5.pack(side=LEFT)
label_6 = Label(frame_bottom, text='Metka6', bg='brown', fg='LightCoral')  # , font=('Arial', 64)
label_6.pack(side=LEFT)

# button_increment = Button(text='NEXT', width=15, height=3)
# button_increment.config(command=change_increment)
# button_increment.pack()

# button_decrement = Button(text='PREVIOUS', width=15, height=3)
# button_decrement.config(command=change_decrement)
# button_decrement.pack()
window.mainloop()
