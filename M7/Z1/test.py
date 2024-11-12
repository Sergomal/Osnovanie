fruits = ["apple", "banana", "cherry", "date"]

print(fruits[:-1])

d = {"a": fruits[0], "b": fruits[1], "c": fruits[2]}


try:
    print(fruits[1])
    print(d.get("q"))
except Exception as e:
    print(e.__class__.__name__)
