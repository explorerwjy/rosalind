from Bio import SeqIO
from sys import argv
from math import factorial

class LONG:
	def long(self,seqlist):
		return pmch = factorial(rna.count('A'))*factorial(rna.count('C'))

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_long.txt'
	seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = LONG()
	print sol.long(seqlist)

