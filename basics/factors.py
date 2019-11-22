# Print factors for the given number

num = int(input("Enter a number :"))

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i, end=' ')

for i in range(10):
    pass

