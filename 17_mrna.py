from codon_table import CodonTable
from sys import argv

class MRNA:
	def __init__(self,codon_table):
		self.codon_table = codon_table
		self.nums = {}
		for k,v in self.codon_table.items():
			if v not in self.nums:
				self.nums[v] = 1
			else:
				self.nums[v] += 1

	def mrna(self,prot):
		total_rna_num = 1
		for i in prot:
			total_rna_num *= self.nums[i]
		return total_rna_num

if __name__=="__main__":
	prot = open(argv[1]).read().strip()+"*"
	codon = CodonTable()
	my_mrna = MRNA(codon.codon_table)
	print my_mrna.mrna(prot)%1000000


