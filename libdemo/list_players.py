players = {}

with  open("players.txt", "rt") as f:
    for line in f:
        parts = line.split(",")
        if len(parts) < 2:
            continue

        players[parts[0]] = int(parts[1])

for name, age in sorted(players.items(), key=lambda t: t[1]):
    print(f"{name:20} {age}")
