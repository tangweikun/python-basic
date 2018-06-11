n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter = counter + 1

print(sum)

var = 1
while var < 2:
    num = int(input('输入一个小数字：'))
    print('你输入的数字是：', num)
    var = var+1
print('good bye')


sites = ['banana', 'apple', 'pear', 'grape']
for site in sites:
    if site == 'pear':
        print('梨出现啦')
        break
    print('' + site)
else:
    print('没有哦')
print('完成循环')

for i in range(len(sites)):
    print(i, sites[i])


for letter in "mayday":
    if letter == 'd':
        break
    print('当前字母为：', letter)

var = 10
while var > 5:
    print('当前变量值为：', var)
    var = var - 2
    if var < 4:
        break
print('hey!')

for letter in "mayday":
    if letter == 'd':
        continue
    print('当前字母为：', letter)

var = 10
while var > -1:
    print('当前变量值为：', var)
    var = var - 2
    if var == 2:
        continue
print('hey!')
