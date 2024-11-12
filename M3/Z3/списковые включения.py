# Синтаксис список = [что сделать for элемент in последовательность if условие]

# заполняем список квадратами чисел от 0 до 10
s = []
for i in range(10):
    s.append(i ** 2)
print(s)

s1 = [i ** 2 for i in range(10)]
print(s1)

# добавляем квадраты только тех чисел, которые больше 3
s2 = [i ** 2 for i in range(10) if i > 3]
print(s2)

s3 = [i * -1 for i in range(30) if i % 2 == 0]
print(s3)

lst = ["i", "like", "python"]

s3 = [item.upper() for item in lst]
print(s3)

s4 = ["@" for i in range(100)]
print(s4)

l1 = [x * x for x in range(10)]
l1 = [x for x in range(0, 20) if x % 2 == 0]

print(l1)

words = ['hello', 'world']
print([word.upper() for word in words])

s = ['apple', 'banana', 'cherry']
print([string[0] for string in s])

hw = ['hello', 'world', 'python']
print([len(word) for word in hw])

s = "Hello, World!"
print(s[7:12]  )
