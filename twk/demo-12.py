list = [1, 2, 3, 4, 5, 2, 2, 1]

print(len(list))

print(max(list))

print(list.count(2))

list.append(8)
print(list)

list.extend([11, 11, 11])
print(list)

print(list.index(11))

list.insert(1, 88)
print(list)

list.pop()
print(list)

list.remove(11)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

copiedList = list.copy()
print(copiedList)

list.clear()
print(list)
print(copiedList)
