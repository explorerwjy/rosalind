<<<<<<< HEAD
#
#Given: An RNA string ss having the same number of occurrences of 'A' as 'U' 
#and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
#Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of ss, 
#modulo 1,000,000.
#na matching is noncrossing as long as there are not edges 

=======
# -*- coding: utf-8 -*-
"""
Catalan Numbers and RNA Secondary Structures
Given: An RNA string ss having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of ss, modulo 1,000,000.
"""
from sys import argv
from Bio import SeqIO

class CAT():
	def __init__(self,seq):
		self.seq = seq
		self.match = {'A':'U','U':'A','C':'G','G':'C'}

	#solution:
	#2 is a noncrossing perfect matching count 1
	#find all the ways to split a sequence into 2 
	def cat(self):
		checked_sequence_list = {}
		return self.haha(self.seq,checked_sequence_list)
		print checked_sequence_list

	def haha(self,sequence,checked_sequence_list):
		if len(sequence) <= 2: #end of recursive
			return 1
		elif sequence in checked_sequence_list: #we already checked this value, return it
			return checked_sequence_list[sequence]
		else: #compute all possible subsequence of this sequence
			sub_sequences = [i for i in range(1,len(sequence),2) if sequence[0]==self.match[sequence[i]] and self.check_seq(sequence[1:i])]
			checked_sequence_list[sequence] = sum([self.haha(sequence[1:i],checked_sequence_list)*self.haha(sequence[i+1:],checked_sequence_list) for i in sub_sequences])
			return checked_sequence_list[sequence]

	def check_seq(self,sequence):
		return (sequence.count('A') == sequence.count('U')) and (sequence.count('C') == sequence.count('G'))

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_cat.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = CAT(seqlist[0])
	print sol.cat()%1000000


