list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

del list[2]
print("删除第三个元素 : ", list)

print(len(list))

print([1, 2, 3]+[3, 4, 5])

print(['H'] * 4)

print(3 in [1, 2, 3])

print(max([1, 2, 3, 5]))

for n in [1, 2, 3, 4]:
    print(n, end=",")
