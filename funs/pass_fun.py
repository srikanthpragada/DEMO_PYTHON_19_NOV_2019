def add(n1, n2):
    return n1 + n2


def multiply(a, b):
    return a * b


def math_op(a, b, fun):
    print(fun(a, b))


math_op(10, 20, add)
math_op(10, 20, multiply)
