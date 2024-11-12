from tkinter import *

window = Tk()
window.title("Я главное окно!")
# window.geometry("300x200")#настраиваем ширину и высоту окна
window.geometry("300x200+500+400")


w = window.winfo_screenwidth()
h = window.winfo_screenheight()
print(f"Размер вашего экрана {w} на {h}")

w2 = w // 2 - 150
h2 = h // 2 - 100

window.geometry(f"300x200+{w2}+{h2}")
window.mainloop()
