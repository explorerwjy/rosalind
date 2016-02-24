import sys

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

    
def process(seq_file_name,table_file_name):
    seq_file = open(seq_file_name)
    table_file = open(table_file_name)
    seq = readseq(seq_file)
    seq = seq.replace('U','T')
    table = readtable(table_file)
    dic,M = makecodon(table)
    poly = translate(seq,dic,1)
    if poly[-1] == "*":
        poly = poly[:-1]
    print poly
    seq_file.close()
    table_file.close()

process(sys.argv[1],sys.argv[2])
