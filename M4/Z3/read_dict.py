file = open("dictionary.txt", 'r', encoding='utf-8')  # , encoding='utf-8' , encoding='windows-1251'
content = file.readline().rstrip().split(":")
print(content)
file.close()
