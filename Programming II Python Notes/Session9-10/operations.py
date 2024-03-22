file_name = "x-file.txt"
fd = open(file_name, "a")
# w is for writing, create an empty file and start writing
# replace with a, a for append, w for write, r for read, with "a" --> you keep adding new things without erasing the old ones

while True:
    line = input("Enter a line (or just press Enter ti quit): ")
    if line:
        fd.write(line + "\n")
    else:
        break

fd.close()