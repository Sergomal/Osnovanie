def count(file_name):
    try:
        with open(file_name, encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


words = count("proba2.txt")
print(f"Количество слов в файле: {words}")
