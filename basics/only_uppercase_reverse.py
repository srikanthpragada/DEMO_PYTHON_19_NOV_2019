
s = input("Enter a string : ")

for c in s[::-1]:
    if c.isupper():   # if ord(c) >= 65 and ord(c) <= 90
        print(c)


