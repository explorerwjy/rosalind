from sys import argv
seq1,seq2 = file(argv[1]).read().split()
l = len(seq1)
if len(seq1) != len(seq2):
	print "error!!"
h=0
for i in xrange(0,l):
	if seq1[i] != seq2[i]:
		h += 1

print h
