
ls = ""
while True:
    s = input("Enter name [end to stop] : ")
    if s == "end":
        break
    if s > ls:
        ls = s


print(ls)


