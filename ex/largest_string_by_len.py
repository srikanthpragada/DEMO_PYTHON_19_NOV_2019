
ls = ""
while True:
    s = input("Enter name [end to stop] : ")
    if s == "end":
        break
    if len(s) > len(ls):
        ls = s


print(ls)


