from sys import argv

def insert(s,pos,ch):
	seq = s[:]
	seq.append(ch)
	while i < pos:
		seq[i] = seq[i-1]
		i -= 1
	seq[i] = ch
	return seq


handle = open(argv[1])
n = int(handle.read())

res = [1]
num = 1
for i in xrange(2,n):
	for j in xrange(i):
		res.append(insert(res[j],j,i))
		num += 1

print num
for i in res:
	if len(i) == n:
		print i


		
