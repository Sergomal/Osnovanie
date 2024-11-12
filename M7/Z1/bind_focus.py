from tkinter import Tk, Entry


def key_press(event):
    print(f"Pressed {event.char}")


def mouse_click(event):
    print(f"Mouse {event.x},{event.y}")


def mouse_move(event):
    print(f"Mouse position {event.x},{event.y}")


def next_widget(event):
    event.widget.tk_focusNext().focus()


window = Tk()
window.geometry("400x400")
window.bind("<Key>", key_press)
window.bind("<MouseWheel>", mouse_click)
window.bind("<Button-1>", mouse_click)
# window.bind("<Motion>", mouse_move)

entry1 = Entry(window)
entry1.pack()
entry2 = Entry(window)
entry2.pack()

entry1.bind("<Tab>", next_widget)


window.mainloop()
