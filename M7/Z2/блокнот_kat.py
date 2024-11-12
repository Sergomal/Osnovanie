from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import transliterate



def delete():
    text.delete(1.0, END)
def insert():
    try:
        file=fd.askopenfilename()
        if file:
            with open(file,"r", encoding="utf-8") as f:
                s=f.read()
        text.insert(1.0, s)
    except FileNotFoundError:
        mb.showerror("Ошибка","Файл не найден")
    except Exception as e:
        mb.showerror("Ошибка",f"Произошла ошибка {e}")

def save():
    try:
        file=fd.asksaveasfilename(filetypes=(("txt file","*.txt"),
                                             ("HTML file","*.html"),
                                             ("All files","*.*")))
        if file:
            with open(file,"w", encoding="utf-8") as f:
                s=text.get(1.0, END)
                f.write(s)
    except FileNotFoundError:
        mb.showerror("Ошибка","Не удалось сохранить файл")
    except Exception as e:
        mb.showerror("Ошибка",f"Произошла ошибка {e}")


def translit_f():
    try:
        s=text.get(1.0,END)
        s_tr=transliterate.translit(s,"ru",reversed=True)
        text.delete(1.0,END)
        text.insert(1.0,s_tr)
    except Exception as e:
        print(f"Я ошибка {e}")

 
window = Tk()
text = Text(width=30, height=8, bg="gray", wrap=WORD)
text.pack(side=LEFT)



scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

menu_bar=Menu(window)
window.config(menu=menu_bar)

file_menu=Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=insert)
file_menu.add_command(label="Сохранить",command=save)
file_menu.add_command(label="Удалить все",command=delete)
file_menu.add_command(label="Транслитерация",command=translit_f)
file_menu.add_command(label="Выход",command=window.destroy)


window.mainloop()
