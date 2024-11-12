import random

m1 = {"Невероятный", "Всемогущий", "Быстроногий", "Могучий"}
m2 = {"Сильнорук", "Быстрокрыл", "Большерот", "Клювоглаз"}
m3 = {"с мечом", "со щитом", "на капибаре", "со стаканом"}

# s1 = random.sample(m1, 3)
# s2 = random.sample(m2, 3)
# s3 = random.sample(m3, 3)
#
# print(s1, s2, s3)

s1 = random.choice(list(m1))
s2 = random.choice(list(m2))
s3 = random.choice(list(m3))

print(f"Супергерой {s1} {s2} {s3}")
