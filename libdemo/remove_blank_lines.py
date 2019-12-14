import os

filename = "names.txt"
target_filename = "temp.txt"

with  open(filename, "rt") as sf:
    with open(target_filename, "wt") as tf:
        for line in sf:
            if len(line.strip()) > 1:
                tf.write(line)

# Delete source file
os.remove(filename)

# Rename target file as source
os.rename(target_filename, filename)
