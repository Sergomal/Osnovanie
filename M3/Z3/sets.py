fruits = {'apple', 'banana', 'cherry'}
print(*fruits)

fruits.discard('something')  # без ошибки
fruits.discard('apple')  # {'banana', 'cherry'}
print(fruits)

print('apple' in fruits)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5, 6, 7, 8}

intersection = set1.intersection(set2)  # {4, 5}
print(intersection)
difference = set1.difference(set2)  # {1, 2, 3}
print(difference)
symmetric_difference = set1.symmetric_difference(set2)  # {1, 2, 3, 6, 7, 8}
print(symmetric_difference)

fruits.remove('banana')
print(fruits)  # {'cherry'}
fruits.remove('cherry')
print(fruits)  # set()
fruits.add('apple')
fruits.add('banana')
fruits.add('cherry')
print(fruits)  # {'cherry', 'apple', 'banana'}
fruits.clear()
print(fruits)  # set()
