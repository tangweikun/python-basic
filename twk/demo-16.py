num = int(input("输入一个数字:"))

if num % 2 == 0:
    if num % 3 == 0:
        print("num be divided by 2 & 3")
    else:
        print("num be divided by 2 but not 3")
else:
    if num % 3 == 0:
        print("num be divided by 3 but not 2")
    else:
        print("num can't be divided by 2 & 3")
