g = 100  # Global variable


def fun():
    global g
    a = 10  # Enclosing variable
    g = 200
    # Local function
    def fun2():
        nonlocal a
        a = a  + 1
        b = 20  # local variable
        print(g, a, b, True)

    fun2()
    print(a)


fun()
