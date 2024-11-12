import datetime

wordz = ["кошка", "аллигатор", "лось", "антилопа", "лосось", "анчоус", "аллигатор", "лось", "антилопа", "лосось",
         "анчоус", "аллигатор", "лось", "антилопа", "лосось", "анчоус", "аллигатор", "лось", "антилопа", "лосось",
         "анчоус"]
t1 = datetime.datetime.now()
f = list(i for i in wordz if i.startswith("а"))
t2 = datetime.datetime.now()
delta_t = t2 - t1
print(delta_t)
print(t1)
print(t2)
print(f)

