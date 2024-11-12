from tkinter import *


def read_login():
    login = login_entry.get()
    print(login)
    login_entry.delete(0, END)


def read_pass():
    password = pass_entry.get()
    print(password)
    pass_entry.delete(0, END)


def read_text():
    text_from_fild = text.get(1.0, END)
    print(text_from_fild)
    text.delete(1.0, END)


def insert_text():
    pushkin = """К *** (Я помню чудное мгновенье…)

Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

В томленьях грусти безнадежной,
В тревогах шумной суеты,
Звучал мне долго голос нежный
И снились милые черты.

Шли годы. Бурь порыв мятежный
Рассеял прежние мечты,
И я забыл твой голос нежный,
Твои небесные черты.

В глуши, во мраке заточенья
Тянулись тихо дни мои
Без божества, без вдохновенья,
Без слез, без жизни, без любви.

Душе настало пробужденье:
И вот опять явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

И сердце бьется в упоенье,
И для него воскресли вновь
И божество, и вдохновенье,
И жизнь, и слезы, и любовь."""
    text_for_insert = text.insert(1.0, pushkin)


def delete_text():
    text.delete(1.0, END)


window = Tk()
# window.geometry('500x500')
window.title("Поле ввода многосторчное")

frame_top = Frame(window)
frame_bottom = Frame(window)
frame_bottom_2 = Frame(window)
frame_top.pack()
frame_bottom.pack()
frame_bottom_2.pack()

login_fild = Label(
    frame_top,
    text="Login:",
    width=9,
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
login_fild.pack(side=LEFT)

login_entry = Entry(
    frame_top,
    width=30,
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
login_entry.pack(side=LEFT)

button_Enter_login = Button(
    frame_top,
    text="Enter",
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
button_Enter_login.config(command=read_login)
button_Enter_login.pack(side=LEFT)

pass_fild = Label(
    frame_bottom, text="Password:", bg="gray", fg="white", font=("Courier", 18, "bold")
)
pass_fild.pack(side=LEFT)
pass_entry = Entry(
    frame_bottom,
    width=30,
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
pass_entry.pack(side=LEFT)

button_Enter = Button(
    frame_bottom,
    text="Enter",
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
button_Enter.config(command=read_pass)
button_Enter.pack(side=LEFT)

text = Text(frame_bottom_2, height=18, width=40, bg="gray", fg="white")
text.pack(side=LEFT)  # , fill=BOTH

scrollbar = Scrollbar(frame_bottom_2, command=text.yview)
scrollbar.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scrollbar.set)

button_Enter_text = Button(
    frame_bottom_2,
    text="Enter",
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
button_Enter_text.config(command=read_text)
button_Enter_text.pack(side=LEFT)

button_Insert_text = Button(
    frame_bottom_2,
    text="Insert",
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
button_Insert_text.config(command=insert_text)
button_Insert_text.pack(side=LEFT)

button_Delete_text = Button(
    frame_bottom_2,
    text="Delete",
    justify="center",
    bg="gray",
    fg="white",
    font=("Courier", 18, "bold"),
)
button_Delete_text.config(command=delete_text)
button_Delete_text.pack(side=LEFT)

window.update()

window.mainloop()
