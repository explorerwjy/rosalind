from sys import argv

handle = open(argv[1])
k,n = map(int,handle.readline().split())
gene = [1]

for i in xrange(1,k):
	
