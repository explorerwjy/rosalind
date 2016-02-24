from sys import argv

handle = open(argv[1])

def rc(seq):
	dic = {'A':'T','T':'A','C':'G','G':'C'}
	return "".join(map(lambda x: dic[x] , [y for y in list(seq)]))

def pal(pos,seq1,seq2):
	i = 0
	ans = []
	while i < 6:
		if pos+i+1 >= len(seq1) or pos-i < 0:
			break
		if seq1[pos-i] == seq2[pos+i+1] and seq1[pos+i+1] == seq2[pos-i]:
			i += 1
			ans.append(i)
		else:
			break
	return ans[::-1]

seq1 = "".join(handle.read().split()[1:])
seq2 = rc(seq1)

ans = {}
for i in xrange(1,len(seq1)-3):
	tmp = pal(i,seq1,seq2)
	#print i,tmp
	for j in tmp:	
		if 2 <= j:
			if i+2-j not in ans:
				ans[i+2-j]=j*2

for k,v in ans.items():
	print k,v




