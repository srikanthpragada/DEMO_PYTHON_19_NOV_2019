def iseven(n):
    # print("Passed ",n)
    return n % 2 == 0


l = [11, 30, 44, 56, 77, 88, 7]

for v in filter(iseven, l):
    print(v)

for c in filter(str.isupper, "Hello PYTHON"):
    print(c)
