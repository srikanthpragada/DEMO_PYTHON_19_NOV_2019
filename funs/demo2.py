def fun():
    print("In fun()")


myfun = fun


def fun(msg):
    print("In fun() with : ", msg)


fun("Abc")
myfun()
