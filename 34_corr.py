#
#Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. 
#Some of these reads were generated with a single-nucleotide error. For each read ss in the dataset, 
#one of the following applies:
#ss was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
#ss is incorrect, it appears in the dataset exactly once, 
#and its Hamming distance is 1 with respect to exactly one correct read in the dataset 
#(or its reverse complement).
#Return: A list of all corrections in the form "[old read]->[new read]". 
#(Each correction must be a single symbol substitution, and you may return the corrections in any order.)

from Bio import SeqIO

class CORR():
	def __init__(self,seqlist):
		self.seqlist = seqlist

	#solution:
	#Groupbythe same sequence
	#check left one as i nuc mutation

	def corr(self):
		#reduce
		unique_seqs = {}
		for seq in seqlist:
			if (seq in unique_seqs) :
				unique_seqs[seq] += 1
			elif (self.rever_com(seq) in unique_seqs):
				unique_seqs[self.rever_com(seq)] += 1
			else:
				unique_seqs[seq] = 1

		unique_seqs = sorted([(k,v) for (k,v) in unique_seqs.items()],key = lambda p:p[1])
		#print unique_seqs

		#refs
		refs = []
		for k,v in unique_seqs:
			if v >=2:
				refs.append(k)

		#errors 
		errors = []
		for k,v in unique_seqs:
			if v == 1:
				errors.append(k)

		#check one nuc mutation from less to many
		for error in errors:
			self.search_right(error,refs)

	def rever_com(self,seq):
		pairs = {'A':'T','T':'A','C':'G','G':'C'}
		return ''.join([pairs[i] for i in seq])[::-1]
	def search_right(self,seq,seq_list):
		#print "poteintail worng seq",seq[0]
		for ref in seq_list:
			if self.Hamming(ref,seq) == 1:
				print "%s->%s"%(seq,ref)
				break
			elif self.Hamming(ref,self.rever_com(seq)) == 1:
				print "%s->%s"%(seq,self.rever_com(ref))
				break

	def Hamming(self,seq1,seq2):
		l = len(seq1)
		if len(seq1) != len(seq2):
			print "error!!"
		h=0
		for i in xrange(0,l):
			if seq1[i] != seq2[i]:
				h += 1
		return h


if __name__ == '__main__':
	small_input = "test.txt"
	large_input = 'D:/Study/rosalind_data/rosalind_corr.txt'
	#seqlist = [str(record.seq) for record in SeqIO.parse(small_input,'fasta')]
	seqlist = [str(record.seq) for record in SeqIO.parse(large_input,'fasta')]
	sol = CORR(seqlist)
	sol.corr()


