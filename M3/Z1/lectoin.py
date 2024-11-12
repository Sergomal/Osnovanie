s1 = [1, 2, 3, 4, 5]
s1.reverse()
s2 = [10, 20, 30, 40, 50]

print(s1)
print(reversed(s2))
for i in reversed(s2):
    print(i)
print(s2)

s1.append(s2)
print(s1)


text = "dfshg. vhfv sjss, fegf!"

print(text.split())
print(list(text))

s1.clear()
c=s1.count(4)

T = tuple('spam')
print(T)

print(s1)
print(c)
