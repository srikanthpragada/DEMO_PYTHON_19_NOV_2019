class A:
    def process(self):
        print("A")


class B(A):
    def process(self):
        print("B")


class C(A, B):
    pass


obj = C()
obj.process()
