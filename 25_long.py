from Bio import SeqIO
from sys import argv

class LONG:
	def long(self,seqlist):
		res = seqlist.pop(0)
		i = 0
		while len(seqlist) > 0:
			seq = seqlist[i]
			length = len(seq)
			
			for j in range(length / 2):
				k = length - j
				if res.startswith(seq[j:]):
					seqlist.pop(i)
					res = seq[:j] + res
					i = 0
				if res.endswith(seq[:k]):
					seqlist.pop(i)
					res = res + seq[k:]
					i = 0
			i += 1
			if i >= len(seqlist):
				i = 0
		return res

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_long.txt'
	seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = LONG()
	print sol.long(seqlist)

