from itertools import count
from sys import argv


script_name, number = argv
number = int(number)
for el in count(number):
    if el > 15:
        break
    else:
        print(el)
