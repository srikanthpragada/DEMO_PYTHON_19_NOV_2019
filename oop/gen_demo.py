def even_numbers(lst):
    for n in lst:
        if n % 2 == 0:
            yield n

n = even_numbers([10, 11, 16, 55, 77, 88])

print(type(n))
# print(next(n))

for v in n:
    print(v)

