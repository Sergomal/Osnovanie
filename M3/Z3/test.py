s = set([1, 2, 3])
s.add(4)
set1 = {2, 3}
e = 4 in s
ss = set1.issubset(s)

print(s, e)
print(ss)

test_dict = {"str": "string", 3.14: "Pi", True: "True", 100: "sto", (1, 2, 3): ("odin", "dva", "tri")}
del test_dict["str"]
print(test_dict)
for value in test_dict.values():
    print(value)
