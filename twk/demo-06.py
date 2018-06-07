# 在混合计算时，Python会把整型转换成为浮点数

print(2 / 4)
print(2 // 4)
print(2 ** 4)
print(2 % 4)
print(2 // 4 + 3)

word = 'hello'
print(word[0], word[-1], word[-5])

list = ['a', 1, '11', True, 4.5]
list2 = ['c', 'c']
print(list[0], list[-1])
print(list[0:2])
print(list[2:])
print(list * 2)
print(list[2] * 2)
print(list + list2)

tuple = (1, '2s', True, '4.4')
print(tuple)
print(tuple[0])
print(tuple[0:2])
print(tuple[1:])
print(tuple * 2)
print(tuple[0:-3])
print(tuple[0:1])
print(tuple[2:3])


student = {'Tom', 'Jack', 'Jane', 'Tom'}
print(student)

if ('Tom' in student):
    print('Tom 在集合中')
else:
    print('Tom不在集合中')

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

c = set('abc')
d = set('cbd')
print(c | d)

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}


print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(tinydict)          # 输出完整的字典
print(tinydict.keys())   # 输出所有键
print(tinydict.values())  # 输出所有值
