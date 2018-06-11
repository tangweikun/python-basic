a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']

for i in range(len(a)):
    print(i, a[i])

print(list(range(4)))


for letter in 'hello world':
    if letter == 'r':
        break
    print('Current letter:', letter)
