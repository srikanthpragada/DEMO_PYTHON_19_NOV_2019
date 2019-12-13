# run from command line as follows:
# python search_files.py pattern startdir

import os
import sys

if len(sys.argv) < 2:
    print("Usage : python search_files.py pattern [startdir]")
    sys.exit(1)

if len(sys.argv) > 2:
    start_dir = sys.argv[2]
else:
    start_dir = "."

pattern = sys.argv[1]

for dirname, dirs, files in os.walk(start_dir):
    for f in files:
        if pattern in f:
            print(dirname + "\\" + f)
