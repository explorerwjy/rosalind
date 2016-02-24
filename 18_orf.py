from my_dna import *
from sys import argv

class ORF:
	def __init__(self,seq):
		self.prots = []
		for frame in ('-1','-2','-3','1','2','3'):
			self.prots.append(translation(seq,frame))
	def orf(self):
		res = []
		for prot in self.prots:
			starts = []
			for i,aa in enumerate(prot):
				if aa == "M":
					starts.append(i)
				
			for start in starts:
				end = 0
				for i in xrange(start,len(prot)):
					if prot[i] == "*":
						end = i
						break
				if end != 0:
					res.append(prot[start:end])
		return res

if __name__=='__main__':
	sequence = "".join(open(argv[1]).read().split()[1:])
	my_orf = ORF(sequence)

	for seq in my_orf.orf():
		print seq
