from sys import argv
import Bio.SeqIO as bioseq
def getgc(seq):
	gg = seq.count("G")
	cc = seq.count("C")
	return 100*float(gg+cc)/len(seq)

handle = open(argv[1])
maxx = 0
maxx_id = ""
for seqr in bioseq.parse(handle, "fasta"):
	tmp = getgc(seqr.seq)
	if tmp > maxx:
		maxx = tmp
		maxx_id = seqr.id
print maxx_id
print "%.6f"%maxx
