def hasdigit(s):
    for c in s:
        if c.isdigit():
            return True
    else:
        return False


items = ["abc", "abc123", "345", "xyz"]
for s in filter(hasdigit, items):
    print(s)
