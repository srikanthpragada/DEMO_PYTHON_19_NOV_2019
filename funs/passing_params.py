def swap(a, b):
    pass


x = 10
y = 20
swap(x, y)
print(x, y)


def zero(v):
    print("Address of v inside zero()", id(v))
    v = 0


def prepend(nums, n):
    nums.insert(0, n)


n = 100
print("Before call to function zero()", id(n))
zero(n)
print(n)

l = [1, 2, 3]
prepend(l, 100)
print(l)
