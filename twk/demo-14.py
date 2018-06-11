a, b = 0, 1

while b < 10:
    temp = a
    a = b
    b += temp
    print(b)
