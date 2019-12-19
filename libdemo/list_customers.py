import re

customers = {}

with open("customers.txt") as f:
    for line in f:
        name = re.search("[A-Za-z ]+", line)
        if name is None:
            continue

        name = name.group().strip()  # Take value from match object

        mobile = re.search("\d+", line)
        if mobile is None:
            continue

        mobile = mobile.group()  # Take value

        if name in customers:
            customers[name].add(mobile)
        else:
            customers[name] = {mobile}

for name, mobiles in sorted(customers.items()):
    print(f"{name:20} {','.join(mobiles)}")
