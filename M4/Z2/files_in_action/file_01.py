# Открываем файл с указанием кодировки UTF-8
file = open('proba.txt', 'r', encoding='utf-8')  # , encoding='utf-8' , encoding='windows-1251'
content = file.read()
print(content)
file.close()
# Видим нормальный текст


try:
    with open("proba2.txt", 'r', encoding="ascii") as file:
        file.write("Некий текст.")
except IOError:
    print("Ошибка ввода-вывода.")
except OSError:
    print("Ошибка операционной системы.")
except UnicodeEncodeError:
    print("Ошибка кодирования текста.")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")

b = "string stroka"
n = b.replace("g s", "rt")
print(n)
