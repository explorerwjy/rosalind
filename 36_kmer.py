#For a fixed positive integer kk, order all possible k-mers taken from an underlying alphabet lexicographically.
#
#Given: A DNA string s in FASTA format (having length at most 100 kbp).
#
#Return: The 4-mer composition of s.

from Bio import SeqIO

class KMER():
	def __init__(self,seq):
		self.seq = seq
		self.seed = ['A','C','G','T']
		self.lexicographical = self.seed
		self.four_mer()

	#Generate 4-mer and alphabet lexicographically
	def four_mer(self):
		for i in range(3):
			tmp = []
			for j in range(len(self.lexicographical)):
				for k in self.seed:
					tmp.append(self.lexicographical[j]+k)
			self.lexicographical = tmp
			del tmp

	def kmer(self):
		composition = []
		for kmer in self.lexicographical:
			composition.append(self.composition(kmer))
		return composition

	def composition(self,kmer):
		count = 0
		for i in range(0,len(self.seq)-3):
			if self.seq[i:i+4] == kmer:
				count +=1
		return str(count)

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_kmer.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = KMER(seqlist[0])
	print " ".join(sol.kmer())