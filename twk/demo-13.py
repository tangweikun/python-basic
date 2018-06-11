tup1 = (1, 2, 3)
tup2 = ("1", "a")
tup3 = 1, 2, 3
print(type(tup1), type(tup2), type(tup3))

tup4 = ()
print(type(tup4))  # <class 'tuple'>

tup5 = (3)
print(type(tup5))  # <class 'int'>

tup6 = (3,)
print(type(tup5))  # <class 'tuple'>

print(len(tup1))

print((1, 2)+(3,))

print(('H',) * 3)

print(3 in (3,))

print(tuple([1, 2, 34]))

print(max(1, 2, 3))

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(len(dict))
print(str(dict))
print(dict.keys())
print(dict.fromkeys)

del dict['Name']
print(dict)
print(type(dict))

dict.clear()
print(dict)

del dict
print(dict)

for n in (1, 2, 3):
    print(n, end=',')
