a = 10
b = 20

if (a and b):
    print("true and true")
else:
    print("at least one false")

if (a or b):
    print("at least one true")
else:
    print("false and false")

a = 0
if (a and b):
    print("true and true")
else:
    print("at least one false")

if (a or b):
    print("at least one true")
else:
    print("false and false")

if not (a and b):
    print("at least one false")
else:
    print("true and true")
