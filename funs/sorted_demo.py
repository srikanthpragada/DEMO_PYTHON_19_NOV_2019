def abs(n):
    return n if n >= 0 else n * -1


l = [11, -30, -44, 56, 77, -88, 7]

for v in sorted(l, key=abs):
    print(v)

names = ['Abcx', 'Abcd', 'Def', 'Xi', 'pqr', 'Ling', 'Joe', 'Abcde']
for s in sorted(names, key=len):
    print(s, end=' ')

print()

for s in sorted(names, key=lambda s: s[:3]):
    print(s, end=' ')
