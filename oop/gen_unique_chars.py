def unique_chars(s1, s2):
    for c in sorted(set(s1 + s2)):
        yield c


for c in unique_chars("Jython", "Python"):
    print(c)
