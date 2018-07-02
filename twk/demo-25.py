def hello():
    print("hello")


hello()


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


def printMe(str):
    print(str)
    return


printMe("我要调用用户自定义函数!")
printMe("再次调用同一函数")


def printinfo(name, age):
    print("名字: ", name)
    print("年龄: ", age)
    return


printinfo(age=50, name="runoob")
