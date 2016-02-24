from Bio import SeqIO
from sys import argv

class LONG:
	def long(self,seqlist):
		while len(seqlist) > 1:
			last = len(seqlist)
			print "Time of while",last
			for seq in seqlist[:-1]:
				tmp = self.gluable(seqlist[-1],seq)
				if tmp != None:
					seqlist.remove(seqlist[-1])
					seqlist.remove(seq)
					seqlist.append(tmp)
					break
			if last == len(seqlist):
				print "Error!"
				break
			print seqlist
		res = seqlist[0]
		return res
	def gluable(self,seq1,seq2):
		if len(seq1) > len(seq2):
			l_seq,s_seq = seq1,seq2
		else:
			l_seq,s_seq = seq2,seq1
		mid = (len(s_seq)+1)/2
		#left:
		p = 0
		while mid - p >= 0:
			if s_seq[mid-p:] == l_seq[0:len(s_seq)-mid-p]:
				return s_seq[0:mid-p] + l_seq
			p+=1
		#middle:
		if l_seq.find(s_seq) >= 0:
			return l_seq
		#right
		p = 0
		while mid + p <= len(s_seq):
			if s_seq[0:mid+p] == l_seq[-(mid+p):]:
				return l_seq + s_seq[mid+p:]
			p+=1
		return None
		
if __name__ == '__main__':
	seqlist = [str(record.seq) for record in SeqIO.parse(argv[1],'fasta')]
	print seqlist
	sol = LONG()
	print sol.long(seqlist)

