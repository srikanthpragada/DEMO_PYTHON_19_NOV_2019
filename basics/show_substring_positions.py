# Find  all positions of substring in mainstring

ms = "This is fine"
ss = "t"

start = 0
while True:
    pos = ms.find(ss,start)
    if pos == -1:
        break

    print(pos)
    start = pos + 1


