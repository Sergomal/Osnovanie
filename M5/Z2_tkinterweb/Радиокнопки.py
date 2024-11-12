from tkinter import *

window = Tk()

kvas = "Квас"
tea = "Чай"
coffee = "Кофе"

drink = StringVar(value=coffee)

m = Label(text="Выбери любимый напиток:")
m.pack()

m2 = Label(textvariable=drink)
m2.pack()


minecraft_b = Radiobutton(text=kvas, value=kvas, variable=drink)
minecraft_b.pack()

roblox_b = Radiobutton(text=tea, value=tea, variable=drink)
roblox_b.pack()

brawl_b = Radiobutton(text=coffee, value=coffee, variable=drink)
brawl_b.pack()
window.mainloop()
