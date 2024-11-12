"""info={"name":"София", "age":11, "rost":155, "animals":True}

print(info)
print(info["name"])#получаем значение по ключу

info['name']="Софья"#изменяем значение словаря по ключу "name"
print(info)

info["school"]=30#добавляем в словарь новый ключ и значение
print(info)

del info["animals"]#удаляем пару из словаря с ключом "animals"
print(info)


#если удалять ключ, которого нет, то получим ошибку
if "animals" in info:#проверяем наличие ключа в словаре
    del info["animals"]
else:
    print("Вы пытаетесь удалить несуществующий ключ")


#ключами могут быть - str, float, bool, int, tuple
([1, 2, 3]: "cpisok" => TypeError: unhashable type: 'list')
({1, 2, 3}: "set" => TypeError: unhashable type: 'list')
#значением может быть все что угодно
"""

# перебор словаря в цикле
test_dict = {"str": "string", 3.14: "Pi", True: "True", 100: "sto", (1, 2, 3): ("odin", "dva", "tri")}
for i in test_dict:  # перебор ключей словаря
    print(i)
dict2 = {"name": "Anton", "age": 23}
test_dict.update(dict2)
print(test_dict)
print(dict2)

info = {"name": "София", "age": 11, "rost": 155, "animals": True}

'''for i in info:#перебор ключей словаря
    print(i)

print()

for i in info.values():#перебор значений словаря
    print(i)'''

for i, j in info.items():  # перебор всех значений словаря
    print(f"Ключ - {i}, значение - {j}")

info2 = {'surname': "Борисова", "patronymic": "Алексеевна", "favorite subject": "информатика"}

info.update(info2)  # расширяем словарь info парами второго словаря
print(info)

'''a={}#создаем пустой словарь
print(type(a))

a1=dict()#создаем пустой словарь
print(type(a1))

s=set()#создаем пустое множество
print(type(s))'''
