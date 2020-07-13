from itertools import cycle
from sys import argv

el1, el2, el3, el4 = argv

iter = cycle([el2, el3, el4])

for i in range(10):
	print(next(iter))
