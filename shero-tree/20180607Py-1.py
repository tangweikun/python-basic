print('my name is %s,I\'m % d years old', ('sherotree', 25))

list1 = ['one', 'two', 'three', 'five']
list2 = [1, 2, 3, 5]

print('list1[1]', list1[1])
print('list2[0:3]', list2[0:3])
list1[1] = 'four'
print('list1[1]', list1[1])
print(list1)
del list1[2]
print(list1)
list3 = [list1, list2]
print(list3)


tup1 = (1, 2, 3)
tup2 = ('th', 'bo', 'po')
tup3 = (tup1, tup2)
print(tup3)
del tup1


dict = {'what': 'ball', 'why': 'because', 'how': "much"}
print('dict["what"]', dict['what'])
print("dict['why']", dict['why'])

dict['what'] = 'key'
print(dict)

del dict['what']
print(dict)
dict.clear()
print(dict)

dict2 = {'open': 'close', 'sun': 'rain', 'sun': 'rainbow'}
print(dict2)
