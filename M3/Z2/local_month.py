import datetime
import locale


locale.setlocale(locale.LC_ALL, '')
d = datetime.date.today()
date = d.strftime("%d %B %Y")

print("Сегодня ", date)
print(locale.getlocale())
