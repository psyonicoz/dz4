from sys import argv
from itertools import count

script_name, start, end = argv
for el in count(int(argv[1])):
    if el > int(argv[2]):
        break
    else:
        print(el)
