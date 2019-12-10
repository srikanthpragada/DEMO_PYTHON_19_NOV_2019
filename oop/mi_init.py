class A:
    def __init__(self):
        print("Type ", type(self))
        print("A")


a = A()


class B:
    def __init__(self):
        print("B")


class C(A, B):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        B.__init__(self)


obj = C()
