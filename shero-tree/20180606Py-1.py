a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, 'sad'
print(a, b, c)

x = 8
y = 3
p = x / y
q = x // y
print(p)
print(q)


list = [123, 'yes', 987, 'what']
tinylist = [567, 'mayday']
print(list)
print(list[1])
print(list[0:4])
print(list[3:])
print(tinylist * 2)
print(list + tinylist)

student = {'bo', 'og', 'ie', 'boogie', 'og'}
print(student)

if ('ie' in student):
    print('iestudent')
else:
    print('ie student')

a = set('poiej')
b = set('diehw')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)


dict = {}
dict['dis'] = 'have'
dict['star'] = 'eat'
tinydict = {'bhg': 'de', 'dte': 'dtw', 'tew': 'wet'}
print(dict['dis'])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
