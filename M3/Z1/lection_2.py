s = [1, 2, 3, 4, 5]
k = (10, 20, 30, 40, 50)
# for i in s:
#     # print(i * 2)
#     s[i] = i * 2
#
# for j in k:
#     print(j / 2)
#     # k[j]=k[j]/2


s.extend(k)
s += k

print(s)
print(k)
print("====================")
print("\t=\t=\t=")
