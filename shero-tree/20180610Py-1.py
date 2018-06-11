# !/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10000:
    print(b, end='\n')
    a, b = b, a+b

age = int(input("input your age："))
print('')
if age < 0:
    print('are you kidding天?')
elif age < 18:
    print('you are a cool teenager!')
elif age < 38:
    print('you are a cool younger!')
elif age < 60:
    print('you are a busy man!')
else:
    print('have a good body!')
