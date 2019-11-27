even_nums =[]
odd_nums = []

while True:
    n = int(input("Enter a number [0 to stop]:"))
    if n == 0:
        break

    if n % 2 == 0:
        even_nums.append(n)
    else:
        odd_nums.append(n)


for n in even_nums + odd_nums:
    print(n)
