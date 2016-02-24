from sys import argv
import math
import random

def my(start):
	return ''.join(start)

n = int(open(argv[1]).read())


start = map(str,range(1,n+1,1))

total_list = {my(start):1}
total = math.factorial(n)
i = 1
while i < total:
	random.shuffle(start)
	#print start
	if my(start) in total_list:
		continue
	else:
		total_list[my(start)] = 1
		i += 1
	#print i
print total
for k,v in total_list.items():
	print " ".join(list(k))
