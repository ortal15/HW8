# A
my_list: list[int] = []
for i in range(1, 100 + 1):
    my_list.append(i)
# B
print(my_list[0])
# C
print(my_list[-1])
# D
print('len', len(my_list))
# E
print(my_list[2:12])
# F
print(my_list[79:])
# G
print(my_list[:18])
# H
print(my_list[::-1])
# I
print(my_list[1:100:2])
# J
print(my_list[2:100:3])
# K
print(my_list[6:100:7])
# L
print(my_list[9:100:10])
# M
print(my_list[98:64:-3])
# N
my_list.insert(50, 999)
print(my_list)
# O
my_list.pop()
print(my_list)
