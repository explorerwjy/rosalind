import sys
import re

def readseq(seq_file):
    seq = ""
    for l in seq_file:
        if l[0] == '>':
            continue
        else:
            seq = seq + l
    return "".join(seq.split())

def readtable(table_file):
    strs = [];
    for i in range(5):
        strs.append(table_file.readline().strip('\n'))
    return strs

def makecodon(strs):
    dic = {}
    M = set()
    base1 = strs[2]
    base2 = strs[3]
    base3 = strs[4]
    starts = strs[1]
    aa = strs[0]
    for i in range(0,len(aa)):
        base = base1[i] + base2[i] + base3[i]
        dic[base] = aa[i]
        if starts[i] == 'M':
            M.add(base)
    return dic,M

def ReMakeCodon(codon,nuc,i):
    tmp = list(codon)
    tmp[i] = nuc
    return ''.join(tmp)
    
def CodonToAA(codon,table):
    codon = codon.upper()
    if codon.count('N') > 1:
        return 'X'
    for i in range(0,3):
        if codon[i] == 'N':
            AA = ReMakeCodon(codon,'A',i)
            for j in "TCG":
                if table[ReMakeCodon(codon,j,i)] != table[AA]:
                    return 'X'
            return table[AA]
    return table[codon]

def translate(seq,table,frame):
    if not (frame == 1 or frame == 2 or frame == 3):
        return False
    poly = []
    for i in range(frame-1,len(seq),3):
        tmp = seq[i:i+3]
        if len(tmp) != 3:
            continue
        poly.append(CodonToAA(tmp,table))
    return "".join(poly)
def rc(seq):
	dic = {"A":"T",'T':'A','C':'G','G':'C'}
	comp = []
	for ch in seq:
		comp.append(dic.get(ch))
	return ''.join(comp)[::-1]
    
def findallseq(seqs,seq):
	seq = re.search('M[\w]*',seq)
        if seq != None:
			seqs.append(seq.group())
			print seq.group()
			findallseq(seqs,seq.group()[1:])
        else:
			return

def process(seq_file_name,table_file_name):
    seq_file = open(seq_file_name)
    table_file = open(table_file_name)
    seq = readseq(seq_file)
    seq = seq.replace('U','T')
    table = readtable(table_file)
    dic,M = makecodon(table)
    seqs = []
    for frams in [1,2,3]:
		poly1 = translate(seq,dic,frams)
		poly2 = translate(rc(seq),dic,frams)
		


		
		
		"""
		print '\n'+poly1	
		#poly1 = re.search('[\w]*',poly1).group()
		#print poly1
		findallseq(seqs,poly1)
		print '\n'+poly2
		#poly2 = re.search('[\w]*',poly2).group()
		#print poly2
		findallseq(seqs,poly2)	
    print "--------------------------------------"
    """
	for seq in seqs:
        print seq
    seq_file.close()
    table_file.close()

process(sys.argv[1],sys.argv[2])
