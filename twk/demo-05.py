# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # True
print(type(A()) == A)  # True
print(isinstance(B(), A))  # True
print(type(B()) == A)  # False
print(type(B()) == A())  # False
