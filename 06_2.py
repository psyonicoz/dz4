from sys import argv
from itertools import cycle

arr = ['a', 'b', 'c', 'd']
script_name, iterations = argv

i = 0
for el in cycle(arr):
    if i > int(argv[1]):
        break
    print(el)
    i += 1
