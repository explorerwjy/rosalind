import sys
from Bio import SeqIO
 
handle = open(sys.argv[1])
for record in SeqIO.parse(handle,"fasta"):
    tmp = record.seq
    break
a,c,g,t=[],[],[],[]
for i in tmp:
    a.append(0)
    c.append(0)
    g.append(0)
    t.append(0)
handle.seek(0)
for record in SeqIO.parse(handle,"fasta"):
    for i,nuc in enumerate(record.seq):
        if nuc == 'A':
            a[i] += 1
        elif nuc == 'C':
            c[i] += 1
        elif nuc == 'G':
            g[i] += 1
        elif nuc == 'T':
            t[i] += 1
con = []
for i in range(0,len(tmp)):
    if max(a[i],c[i],g[i],t[i]) == a[i]:
        con.append('A')
    elif max(a[i],c[i],g[i],t[i]) == g[i]:
        con.append('G')
    elif max(a[i],c[i],g[i],t[i]) == c[i]:
        con.append('C')
    elif max(a[i],c[i],g[i],t[i]) == t[i]:
        con.append('T')
print "".join(con)
print "A:",
for i in a:
    print i,
print "\nC:",
for i in c:
    print i,
print "\nG:",
for i in g:
    print i,
print "\nT:",
for i in t:
    print i,
    
