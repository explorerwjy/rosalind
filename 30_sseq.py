from sys import argv
from Bio import SeqIO

class SSEQ:
	def sseq(self,seq1,seq2):
		p1 = 0
		p2 = 0
		indice = []
		while p1 < len(seq1) and p2 < len(seq2):
			if seq1[p1] == seq2[p2]:
				indice.append(p1+1)
				p2 += 1
			p1 += 1
		return indice

if __name__=='__main__':
	seqs = []
	for seq in SeqIO.parse(argv[1],'fasta'):
		seqs.append(seq)
	seq1 = str(seqs[0].seq)
	seq2 = str(seqs[1].seq)
	my_sseq = SSEQ()
	res = my_sseq.sseq(seq1,seq2)
	for i in res:
		print i,
