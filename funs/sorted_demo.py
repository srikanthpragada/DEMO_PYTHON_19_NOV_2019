def abs(n):
    return n if n >= 0 else n * -1


l = [11, -30, -44, 56, 77, -88, 7]

for v in sorted(l, key=abs):
    print(v)

names = ['Abcd', 'Def', 'Xi', 'pqr', 'Ling', 'Joe']
for s in sorted(names, key=len):
    print(s, end=' ')
