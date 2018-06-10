a = 10
b = 20
c = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("a in list")
else:
    print("a not in list")

if (b not in list):
    print("b not in list")
else:
    print("b in list")

if (b is c):
    print("b is c")
else:
    print("b not is c")

if (id(b) == id(c)):
    print("id(b) == id(c)")
else:
    print("id(b) != id(c)")

c = 30


if (b is c):
    print("b is c")
else:
    print("b not is c")

if (id(b) == id(c)):
    print("id(b) == id(c)")
else:
    print("id(b) != id(c)")
