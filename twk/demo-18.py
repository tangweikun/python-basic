counter = 0

while counter < 5:
    print(counter)
    counter += 1
else:
    print('exit')

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)

sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


for n in range(5):
    print(n)

for m in range(3, 8):
    print(m)

for j in range(1, 8, 3):
    print(j)
