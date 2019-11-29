depts = {}
while True:
    deptno = int(input("Enter department number [0 to stop] :"))
    if deptno == 0:
        break

    name = input("Enter employee name :")

    if deptno in depts:
        depts[deptno].append(name)  # Add to existing list
    else:
        depts[deptno] = [name]  # Add new dept with list

for deptno, names in sorted(depts.items()):
    print(deptno, ",".join(sorted(names)))
