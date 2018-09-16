a = int(input())
s = 0
while s != 1:

    b = a % 10
    while a >= 10:
        m2 = b ** 2
        b = a/10
        s = m2 + s
    if (s == 1):
        break
