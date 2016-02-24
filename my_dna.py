def get_codon_table():
	codon_table = {
	'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
	'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
	'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
	'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
	'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
	'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
	'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
	'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
	'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
	'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
	'TAA': '*',     'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
	'TAG': '*',     'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
	'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
	'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
	'TGA': '*',     'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
	'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'}
	return codon_table

def compliment(seq):
	nucs = {'A':'T','T':'A','C':'G','G':'C'}
	return "".join(map(lambda x:nucs[x],[y for y in list(seq)]))

def translation(seq,frame):
	codon_table = get_codon_table()
	if frame[0]=='-':
		frame = (int(frame[1])-1%3)+1
		seq = compliment(seq)[::-1]
	else:
		frame = (int(frame)-1%3)+1
	prot = []
	for i in xrange(frame-1,len(seq),3):
		if len(seq[i:i+3])==3:
			prot.append(codon_table[seq[i:i+3]])
		else:
			break
	return "".join(prot)
	

if __name__=='__main__':
	codon = CodonTable()
	print "hello"
	print codon.test
	print codon.codon_table
	print codon.get_codon_table()
