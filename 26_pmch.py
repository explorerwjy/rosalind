from Bio import SeqIO
from sys import argv
from math import factorial
class rosalind_pmch:
	def pmch(self,seq):
		return factorial(seq.count('A'))*factorial(seq.count('C'))

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_pmch.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	seq = seqlist[0]
	sol = rosalind_pmch()
	print sol.pmch(seq)