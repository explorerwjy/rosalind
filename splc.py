import sys
import re
from Bio import SeqIO

DNA_CODON_TABLE = {
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

def translation(sequence,table):
	prot = []
	for i in range(0,len(sequence),3):
		codon = sequence[i:i+3]
		if len(codon) == 3:
			prot.append(table[codon])
		else:
			return prot
		if prot[-1] == "*":
			prot.pop(-1)
	return "".join(prot)
seqs = []
for record in SeqIO.parse(sys.argv[1],"fasta"):
	seqs.append(record.seq)
my_seq = seqs[0]

for intron in seqs[1:]:
	start = my_seq.find(intron)
	if start != -1:
		my_seq = my_seq[0:start] + my_seq[start+len(intron):]

#print my_seq
print translation(my_seq,DNA_CODON_TABLE)

