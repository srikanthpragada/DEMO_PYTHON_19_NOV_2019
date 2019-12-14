with  open("names.txt", "rt") as f:
    for name in sorted(set(f.readlines())):
        print(name, end='')
