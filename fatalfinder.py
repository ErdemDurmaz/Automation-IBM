import re
fhandler = input('Heyo! Insert the exact name of the file: ')
for line in fhandler:
    line = line.rstrip()
    if re.search('^fatal:', line):
        print(line)
