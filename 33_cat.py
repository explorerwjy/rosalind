# -*- coding: utf-8 -*-
"""
Catalan Numbers and RNA Secondary Structures
Given: An RNA string ss having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of ss, modulo 1,000,000.
Solution: cn=∑nk=1ck−1⋅cn−kcn=∑k=1nck−1⋅cn−k . The resulting numbers cncn counting noncrossing perfect matchings in K2nK2n are called the Catalan numbers
"""
from sys import argv
from Bio import SeqIO

class CAT():
	def __init__(self,seq):
		self.nodes = len(seq)
		if self.nodes%2 != 0:
			print "Not valid node number"

	def new(self,sequence):
		tmp = 0
		for i in range(len(sequence)):
			tmp += sequence[i-1]*sequence[-i]
		return tmp

	def catalan(self):
		sequence = [1]
		i = 1
		while i <= self.nodes/2:
			i += 1
			sequence.append(self.new(sequence))
		print sequence
		return sequence[-1]%1000000

if __name__=='__main__':
	small_input = 'test.txt'
	large_input = 'rosalind_cat.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = CAT(seqlist[0])
	print sol.catalan()
