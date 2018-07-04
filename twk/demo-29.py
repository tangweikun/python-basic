for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
