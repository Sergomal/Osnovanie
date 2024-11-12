fr = {"orange", "banana", "peach"}  # неупорядоченная коллекция уникальных данных

print(fr)
print(type(fr))

fr.add("cherry")  # добавляем элемент в множество
print(fr)

fr.discard("banana")  # удаляем элемент из мно-ва

print("banana" in fr)  # проверяем есть ли искомый элемент в множестве

# операции с множествами

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

s_uni = s1.union(s2)  # объединение
print(s_uni)
# получили новое мн-во с элементами из обоих мн-в


s_inter = s1.intersection(s2)  # пересечение
print(s_inter)
# элементы, которые входят и в одно, и во второе мн-во одновременно


s3 = {3, 2, 4}
s_iss = s3.issubset(s1)
# проверяем является ли мн-во s3 подмножеством s1
print(s_iss)

print(s2.issubset(s1))  # здесь получается False

fr.clear()  # очищаем множество
print(fr)
