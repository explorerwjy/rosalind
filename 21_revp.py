from my_dna import *
from sys import argv

class REVP:
	def revp(self,seq1):
		l = len(seq1)
	#	print l
		seq2 = compliment(seq1)
	#	print seq1
	#	print seq2
		res = []
		for i in xrange(1,l-2):
	#		print i
			j = 0
			while j <= 6 and i-j >= 0 and i+j+1 < l :
				if seq1[i-j] == seq2[i+j+1] and seq1[i+j+1] == seq2[i-j]:
					j += 1
					if j >= 2:
						res.append([i-j+2,j*2])
				else:
					break
		
		return res
	def revp2(self,seq):
		l = len(seq)
		res = []
		for i in xrange(0,l):
			for j in range(4,13):
				if i+j>l:
					continue
				sub1 = seq[i:i+j]
				sub2 = compliment(sub1)[::-1]
				if sub1==sub2:
					res.append([i+1,j])
		return res

if __name__=="__main__":
	seq = "".join(open(argv[1]).read().split()[1:])
	my_revp = REVP()
	res = my_revp.revp2(seq)
	for item in res:
		print item[0],item[1]
