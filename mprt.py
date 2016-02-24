from sys import argv
import re
import urllib

handle = open(argv[1])
root = 'http://www.uniprot.org/uniprot/'
for entry in handle:
	url = root + entry.strip() +'.fasta'
	fasta = urllib.urlopen(url).read()
	seq = ''.join(fasta.split('\n')[1:])
	pos = []
	for i in xrange(0,len(seq)-4):
		match = re.search("N[^P][ST][^P]",seq[i:i+4])
		if match != None:	
			pos.append(i+1)
	"""
	for match in re.finditer("N[^P][ST][^P]",seq):
		pos.append(match.start()+1)
	"""
	if len(pos)!=0:
		print entry.strip()
		for item in pos:
			print item,
		print
	

