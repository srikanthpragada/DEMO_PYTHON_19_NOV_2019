squares = []

for n in range(1, 11):
    squares.append(n * n)

print(squares)

cubes = [n**3 for n in range(1,11) if n % 2 == 0 ]
print(cubes)
