import os

start_dir = r"e:\classroom\python\nov19"

for dirname, dirs, files in os.walk(start_dir):
    for f in files:
        if f.endswith(".py"):
            print(dirname + "\\" + f)
