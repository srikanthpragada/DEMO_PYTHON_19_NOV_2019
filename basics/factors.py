# Print factors for the given number on command line

import sys

num = int(sys.argv[1])

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i, end=' ')

print()

