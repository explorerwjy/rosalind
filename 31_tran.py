from Bio import SeqIO
from sys import argv

class TRAN:
	def tran(self,seqlist):
		seq1 = seqlist[0]
		seq2 = seqlist[1]
		length = len(seq1)
		transitions,transversions = 0,0
		for i in xrange(length):
			if seq1[i] != seq2[i]:
				if ((seq1[i] == 'A' and seq2[i] == 'G') or (seq1[i] == 'G' and seq2[i] == 'A') or (seq1[i] == 'C' and seq2[i] == 'T') or (seq1[i] == 'T' and seq2[i] == 'C')):
					transitions += 1
				else:
					transversions += 1
		return round(float(transitions)/transversions,11)

if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_tran.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = TRAN()
	print sol.tran(seqlist)

