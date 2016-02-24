from sys import argv

handle = open(argv[1])
n,m = map(int,handle.readline().split())
rabbits = [1,1]
i = 2
while i< n:
	if(i<m):
		rabbits.append(rabbits[-2]+rabbits[-1])	
	elif (i==m or i==m+1):
		rabbits.append(rabbits[-2]+rabbits[-1]-1)
	else:
		rabbits.append(rabbits[-2]+rabbits[-1]-rabbits[-m-1])
	print rabbits
	i+=1

print rabbits
