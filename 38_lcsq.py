#Given: A DNA string ss (of length at most 100 kbp) in FASTA format.
#Return: The failure array of s.
from Bio import SeqIO
from sys import argv

class LCSQ():
	def __init__(self,seq):
		self.seq = seq
		self.prefix = []
		self.length = len(self.seq)

	def lcsq(self):
		a = 0
		self.prefix = [0]*self.length
		for j in range(2,self.length):
			while a > 0 and self.seq[a] != self.seq[j-1]:
				a = self.prefix[a-1]
			if self.seq[a] == self.seq[j-1]:
				a += 1
			self.prefix[j-1] = a
		return self.prefix

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_kmp.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = LCSQ(seqlist[0])
	print ' '.join(map(str,sol.kmp_prefix()))


