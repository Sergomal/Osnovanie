import random

# for i in range(10):
#     print("\n")
#     for j in range(10):
#         n = random.randint(0, 1000)
#         print(str(n), end="\t")

for i in range(10):
    a1 = (random.randint(0, 9))
    a2 = (random.randint(0, 99))
    a3 = (random.randint(0, 9999))
    print(f"|{a1: > 6}\t|{a2: > 6}\t|{a3: > 6}\t|")
