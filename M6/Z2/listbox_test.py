from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("500x200")

languages = ["Python", "JavaScript", "C#", "Java"]
languages_var = Variable(value=languages)

languages_listbox = Listbox(listvariable=languages_var)

languages_listbox.pack(side=LEFT, anchor=NW, fill=X, padx=5, pady=5)

languages_year = ["1980", "1990", "2000", "2010"]
languages_year_var = Variable(value=languages_year)

languages_year_listbox = Listbox(listvariable=languages_year_var)

languages_year_listbox.pack(side=LEFT, anchor=NE, fill=X, padx=5, pady=5)




root.mainloop()
