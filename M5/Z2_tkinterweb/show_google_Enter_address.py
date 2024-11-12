from tkinter import *
import tkinterweb


def read():
    Site = entry_address.get()
    frame.load_website(Site)


window = Tk()

frame_top = Frame(window)
frame_bottom = Frame(window)
frame_top.pack()
frame_bottom.pack()

label_address = Label(frame_top, text="Enter the website address:")
label_address.pack(side=LEFT)
entry_address = Entry(frame_top, width=20, justify="left")
entry_address.pack(side=LEFT)
button_enter = Button(frame_top, text="Enter", command=read)
button_enter.pack(side=LEFT)
frame = tkinterweb.HtmlFrame(window, frame_bottom)
frame.load_website("https://www.google.com")
frame.pack(fill="both", expand=1)
window.mainloop()
